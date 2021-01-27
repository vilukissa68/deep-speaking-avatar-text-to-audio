# Deep Speaking Avatar - Text-to-Audio
This project is part of Deep Speaking Avatar project (link here)


## Building the documentation
```bash
cd documentation
make all
make clean
```

## Dependencies
### Python dependencies
Python dependencies can be installed by running
```bash
pip install dependencies.txt
pip install theano
```

### C++ dependencies
This project uses [[https://github.com/SPEECHCOG/Merlin_GlottDNN_synth][Merlin_GlottDNN_synth]] for the neural network and it has some C++ dependencies. To install these dependencies on Arch Linux run this command: 
```bash
pacman -S gsl libsndfile libconfig
```

## Compiling
Some parts of the Merlin+GlottDNN need to be compile before use:
```bash
./src/Merlin_GlottDNN_synth/tools/compile_other_speech_tools.sh
```
