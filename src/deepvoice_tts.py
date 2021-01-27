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
import sounddevice as sd
import matplotlib.pyplot as plt

NAME = "deepvoice3_pytorch"

# Git branch for pre-trained model
BRANCH = "abf0a21"

# Project root location CHANGE THIS ON NEW SYSTEM!!!
ROOT = "/home/vaino/deep-speaking-avatar-text-to-audio/"

# Pretrained model information
PRESET = "20180505_deepvoice3_ljspeech.json"
CHECKPOINT = "20180505_deepvoice3_checkpoint_step000640000.pth"

# Alias Declarations
fs = 22050
hop_length = 256

"""
This functions sets up the environment to use DeepVoice3 and get model
"""
def setup():
    os.chdir(ROOT)
    if not exists(NAME):
        url = "https://github.com/r9y9/" + NAME
        os.system("git clone %s" % url)
    os.chdir(NAME)
    os.system("pip install -q -e \'.[bin]\'") # THIS MIGHT NOT WORK: TEST
    #os.system("./dependency_scipt.sh") # Install python dependcies
    #os.system("./dependency_scipt.sh") # Install bash dependcies
    os.system("python -m nltk.downloader cmudict") # English text processing 

    # Get the model
    os.system("git checkout %s --quiet" % BRANCH)

    if not exists(PRESET):
        url = "https://www.dropbox.com/s/0ck82unm0bo0rxd/" + PRESET
        os.system("curl -O -L %s" % url)
    if not exists(CHECKPOINT):
        url = "https://www.dropbox.com/s/5ucl9remrwy5oeg/" + CHECKPOINT
        os.system("curl -O -L %s" % url)

    # Hyper parameters
    import hparams
    import json

    # Load parameters from preset
    with open(PRESET) as f:
        hparams.hparams.parse_json(f.read())

    # Inject frontend text processor
    import synthesis
    import train
    from deepvoice3_pytorch import frontend
    synthesis._frontend = getattr(frontend, "en")
    train._frontend =  getattr(frontend, "en")

    # alises
    fs = hparams.hparams.sample_rate
    hop_length = hparams.hparams.hop_size
    print(os.path.dirname(os.path.realpath(__file__)))

    # Load model
    from train import build_model
    from train import restore_parts, load_checkpoint

    print("Building model")
    model = build_model()
    model = load_checkpoint(CHECKPOINT, model, None, True)
    return model

def tts(model, text, p=0, speaker_id=None, fast=True, figures=True):
    from synthesis import tts as _tts
    waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
    if figures:
        visualize(alignment, spectrogram)
    sd.play(waveform, 22500)
    sd.wait()


def visualize(alignment, spectrogram):
  label_fontsize = 16
  plt.figure(figsize=(16,16))

  plt.subplot(2,1,1)
  plt.imshow(alignment.T, aspect="auto", origin="lower", interpolation=None)
  plt.xlabel("Decoder timestamp", fontsize=label_fontsize)
  plt.ylabel("Encoder timestamp", fontsize=label_fontsize)
  plt.colorbar()

  plt.subplot(2,1,2)
  librosa.display.specshow(spectrogram.T, sr=fs, 
                           hop_length=hop_length, x_axis="time", y_axis="linear")
  plt.xlabel("Time", fontsize=label_fontsize)
  plt.ylabel("Hz", fontsize=label_fontsize)
  plt.tight_layout()
  plt.colorbar()
  plt.show()

model = setup()
text = "Copypasta can usually be found posted in a discussion about any subject, and will usually be intended to draw out newer users into responding negatively to it, much to the amusement of more veteran users."
tts(model, text, speaker_id=None ,figures=False)
print("Done")
