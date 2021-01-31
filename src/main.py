import sounddevice as sd


MULTI = True
if MULTI:
    import multivoice
else:
    import synthesizer



def loop():
    if MULTI:
        model, vocoder_model, CONFIG, use_cuda, ap, speaker_fileid, speaker_embedding = multivoice.setup() # Load module
        speaker_embedding = multivoice.getSpeaker(6) # Set speaker
        gst_style = {"0": -0.5, "1": 0.5, "3": 0.5, "4": 2} # Use custom gst style
    else:
        model, vocoder_model, speaker_id, CONFIG, use_cuda, ap = synthesizer.setup()
    while True:
        sentence = input("Tell me something:")
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
                                 gst_style=None)
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

loop()
