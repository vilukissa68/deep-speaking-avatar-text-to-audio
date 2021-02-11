import sounddevice as sd
import integration
import time

MULTI = True
if MULTI:
    import multivoice
else:
    import synthesizer



def loop():
    if MULTI:
        model, vocoder_model, CONFIG, use_cuda, ap, speaker_fileid, speaker_embedding = multivoice.setup() # Load module
        speaker_embedding = multivoice.getSpeaker(26) # Set speaker
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
        lines = integration.check_file() 
        if len(lines) > 0:
            for sentence in lines:
                if sentence == "q":
                    return

                if MULTI:
                    wav = multivoice.tts(model,

                                        vocoder_model,
                                        sentence,
                                        CONFIG,
                                        use_cuda,
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
                                                            use_cuda,
                                                            ap,
                                                            use_gl=False,
                                                            figures=True)
                sd.play(wav, 22050)
                sd.wait()
        else:
            print("Waiting for changes in file files/in.txt")
            time.sleep(1)
            
        

loop()
