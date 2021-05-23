import sounddevice as sd
import soundfile as sf
import sys
import time
import multivoice
import integration


USE_CUDA = False
MULTI = True
SPEAKER = 26
READLOCATION = "/home/vaino/sound.txt"
WRITELOCATION = "/home/vaino/sound.wav"
FLAGFILE = "/home/vaino/speaking.txt" # Other modules read this file to know if avatar is speaking
POLLINGRATE = 10 # Times polled in one second
SPEAKINGFLAG = False
WRITETOFILE = False


def setup(args):
    if("--cuda" in args):
        global USE_CUDA
        USE_CUDA = True

    if("--speaker" in args):
        i = args.index("--speaker")
        number_of_speakers = multivoice.getNumberOfSpeakers()
        if(i+1 < len(args)):
            tmp = int(args[i + 1])
            if ((tmp < number_of_speakers) and (tmp > 0)):
                global SPEAKER
                SPEAKER = tmp
            else:
                print("Invalid speaker, defaulting to 1")
                SPEAKER = 1
        else:
            print("Please give speaker number after argument")
            return 0

    if("--polling-rate" in args):
        i = args.index("--polling-rate")
        if(i+1 < len(args)):
            global POLLINGRATE
            POLLINGRATE = args[i+1]

    if("--write-to-file" in args):
        global WRITETOFILE
        WRITETOFILE = True

    if("-w" in args):
        i = args.index("-w")
        if(i+1 < len(args)):
            global WRITELOCATION
            WRITELOCATION = args[i+1]

    if("-r" in args):
        i = args.index("-r")
        if(i+1 < len(args)):
            global READLOCATION
            READLOCATION = args[i+1]

    if("--single" in args):
        MULTI = False
        import synthesizer
    else:
        MULTI = True

    if("--list-speakers" in args):
        multivoice.listSpeakers()
        return 0
    return 1

def loop():
    integration.write_file("0", FLAGFILE) # Create flagfile
    if MULTI:
        model, vocoder_model, CONFIG, ap, speaker_fileid, speaker_embedding = multivoice.setup(USE_CUDA) # Load module
        speaker_embedding = multivoice.getSpeaker(CONFIG, choice=SPEAKER) # Set speaker
        # 0: Word pauses
        # 1: Word start timing?
        # 2: ???
        # 3: Speed
        # 4: Volume minus: louder plus: quiter
        gst_style = {"0": 0.1, "1": 0.1, "2": 0, "3": -0.1, "4": -0.2} # Use custom gst style
    else:
        model, vocoder_model, speaker_id, CONFIG, use_cuda, ap = synthesizer.setup()
    while True:
        # sentence = input("Tell me something:")
        lines = integration.check_file(READLOCATION)
        if len(lines) > 0:
            for sentence in lines:
                if sentence == "q":
                    return

                if MULTI:
                    print("speaker:", multivoice.getSpeakerId(SPEAKER), "gst:", gst_style)
                    wav = multivoice.tts(model,

                                        vocoder_model,
                                        sentence,
                                        CONFIG,
                                        USE_CUDA,
                                        ap,
                                        True,
                                        speaker_fileid,
                                        speaker_embedding,
                                        gst_style=gst_style)
                else:
                    align, mel, stops, wav = synthesizer.tts(sentence,
                                                            model,
                                                            vocoder_model,
                                                            speaker_id,
                                                            CONFIG,
                                                            USE_CUDA,
                                                            ap,
                                                            use_gl=False,
                                                            figures=True)
                integration.write_file("1", FLAGFILE)
                sd.play(wav, 22050)
                if(WRITETOFILE):
                    integration.write_soundfile(wav, WRITELOCATION, 22050)
                sd.wait()
                integration.write_file("0", FLAGFILE)
        else:
            print("Waiting for changes in file", READLOCATION)
            time.sleep(1/POLLINGRATE)


# State variable can be used to prevent the module from starting
state = setup(sys.argv)
if (state):
    loop()
