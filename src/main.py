import sounddevice as sd
import soundfile as sf
import sys
import time
import multivoice
import integration


USE_CUDA = True
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
        if(i+1 < len(args)):
            global SPEAKER
            SPEAKER = int(args[i + 1])
        else:
            print("Please give speaker number after argument")
            return
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
            print("WRITE LOCATION SET", WRITELOCATION)

            if("-r" in args):
        i = args.index("-r")
        if(i+1 < len(args)):
            global READLOCATION
            READLOCATION = args[i+1]

    if("--single" in args):
        MULTI = False
        import synthesizer
    else:
        print("Import multivoice")
        MULTI = True


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
                    sf.write(WRITELOCATION, wav, 22050)
                sd.wait()
                integration.write_file("0", FLAGFILE)
        else:
            print("Waiting for changes in file", READLOCATION)
            time.sleep(1/POLLINGRATE)

setup(sys.argv)
loop()
