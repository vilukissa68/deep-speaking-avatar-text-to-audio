# Deep Speaking Avatar - Text-to-Audio
This project is part of Deep Speaking Avatar project (link here)


## Building the documentation
```bash
cd documentation
make all
make clean
```

## Dependencies

Synthesizer only tested to work on python 3.8. To install python 3.8 it's recommended to use conda virtual enviroment.

```bash
sudo apt-get install espeak
```

### Espeak
Espeak is needed for the audio synthesis. It can be installed as a binary on debian based distros via:

```bash
sudo apt-get install espeak
```
For non-debian based distributions your package manager might or might not have epseak.

## Usage
First run 'setup_multispeech.sh' to get all the needed dependencies to run the synthesizer

```bash
./src/setup_multivoice.sh
```

After the environment is setup the synthesizer can be run with: 
```bash
python3.8 src/multivoice.py
```

