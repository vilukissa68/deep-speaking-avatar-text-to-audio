tts --text "Hello Antti nice to meet you" \
    --model_name "tts_models/en/ljspeech/tacotron2-DCA" \
    --vocoder_name "vocoder_models/en/ljspeech/mulitband-melgan" \
    --out_path "/home/vaino/synth/" \
    --use_cuda USE_CUDA
