"""
This file does all the TTS stuff
"""

import os
from os.path import exists

# Might need to reposition this
import torch
import numpy as np
import librosa
import librosa.display


NAME = "deepvoice3_pytorch"

# Git branch for pre-trained model
BRANCH = "abf0a21"

# Project root location CHANGE THIS ON NEW SYSTEM!!!
ROOT = "~/home/vaino/deep-speaking-avatar-text-to-audio"

# Pretrained model information
PRESET = "20180505_deepvoice3_ljspeech.json"
CHECKPOINT = "20180505_deepvoice3_checkpoint_step000640000.pth"

"""
This functions sets up the environment to use DeepVoice3 and get model
"""
def setup():
    os.chdir(ROOT)
    if not exists(NAME):
        url = "https://github.com/r9y9/" + NAME
        os.system("git clone ‰s" % url)
    os.chdir(NAME)
    os.system("pip install -q -e \'.[bin]\'") # THIS MIGHT NOT WORK: TEST
    #os.system("./dependency_scipt.sh") # Install python dependcies
    #os.system("./dependency_scipt.sh") # Install bash dependcies
    os.system("python -m nltk.downloader cmudict") # English text processing 

    # Get the model
    os.system("git checkout ‰s --quite" % BRANCH)

    if not exists(PRESET):
        url = "https://www.dropbox.com/s/0ck82unm0bo0rxd/" + PRESET
        os.system("curl -O -L %s" % url)
    if not exists(CHECKPOINT):
        url = "https://www.dropbox.com/s/5ucl9remrwy5oeg/" + CHECKPOINT
        os.system("curl -O -L %s" % url)

    # Load model
    from train import build_model
    from train import restore_parts, load_checkpoint

    model = build_model()
    model = load_checkpoint(CHECKPOINT, model, None, True)
    return model

def tts(model, text, p=0, speaker_id=None, fast=True, figures=False):
    from synthesis import tts as _tts
    waveform , alignment, spectorgram, mel = _tts(model, text, p, speaker_id, fast)
    return waveform
