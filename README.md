# Deep Speaking Avatar - Text-to-Audio
This project is part of Deep Speaking Avatar project (link here)

## Dependencies

Synthesizer only tested to work on python 3.8. To install python 3.8 it's recommended to use conda virtual enviroment.

### Espeak
Espeak is needed for the audio synthesis. It can be installed as a binary on debian based distros via

```bash
sudo apt-get install espeak
```
For non-debian based distributions your package manager might or might not have epseak.

## Usage
First run 'setup_multispeech.sh' to get all the needed dependencies to run the synthesizer

```bash
./src/setup_multivoice.sh
```

After the environment is setup the synthesizer can be run with 
```bash
python3.8 src/main.py
```

## Parameters
Use CUDA
```bash
python src/main.py --cuda
```

List VCTK speakers
```bash
python src/main.py --list-speakers
```


Set VCTK speaker
```bash
python src/main.py --speaker 10
```

Define polling rate for readfile. Polling rate is given as n-times per second.
```bash
python src/main.py --polling-rate 100
```

Define read- and writefiles
```bash
python src/main.py -w /path/to/writefile -r /path/to/readfile
```



