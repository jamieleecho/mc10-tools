# mc10-tools

This is a simple collection of tools to assist with developing software for
the [TRS-80 Microcolor Computer MC-10](https://en.wikipedia.org/wiki/TRS-80_MC-10).


## Installation
```
git clone https://github.com/jamieleecho/mc10-tools.git
cd mc10-tools
python3 setup.py
```


## Tools
### c10tobas
```
Usage: c10tobas [OPTIONS] INPUT_FILE OUTPUT_FILE

  Extract and detokenizes the *.bas file in INPUT_FILE and stores it in
  OUTPUT_FILE

Options:
  --version  Show the version and exit.
  --help  Show this message and exit.
```

### bastoc10
```
Usage: bastoc10 [OPTIONS] INPUT_FILE OUTPUT_FILE

  Tokenizes the given *.bas file specified byt INPUT_FILE, outputing the
  result into a *.c10 file specified by OUTPUT_FILE.

Options:
  --version  Show the version and exit.
  --help  Show this message and exit.
```


## Developing and Testing
```
# Build the docker image
docker-compose build test

# Run tests using the source on the docker image
docker-compose run test

# Run tests using the source on the host computer
docker-compose run testv

# Run a shell using the source on the docker image
docker-compose run bash

# Run a shell using the source on the host computer
docker-compose run bashv

```
