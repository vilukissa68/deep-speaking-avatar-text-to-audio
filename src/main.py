import sounddevice as sd
import synthesizer


def loop():
    model, vocoder_model, speaker_id, CONFIG, use_cuda, ap = synthesizer.setup()
    while True:
        sentence = input("Tell me something:")
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
