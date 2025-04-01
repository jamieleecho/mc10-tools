# mc10-tools

This is a simple collection of tools to assist with developing software for
the [TRS-80 Microcolor Computer MC-10](https://en.wikipedia.org/wiki/TRS-80_MC-10).


## Installation
```bash
git clone https://github.com/jamieleecho/mc10-tools.git
cd mc10-tools
make install-pre-commit
make install
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

You will need a fairly modern python environment with [uv](https://github.com/astral-sh/uv) installed.

You can begin by entering:
```bash
make install-pre-commit
make sync
make run-tests
```

The `Makefile` makes it easy to perform the most common operations:
* `make check-all` runs linting and `uv.lock` checks
* `make check-lint` checks for linting issues
* `make check-lock` verifies the `uv.lock` is aligned to `pyproject.toml`
* `make clean` cleans the virtual environment and caches
* `make default` runs a default set of checks on the code
* `make fix-all` formats the code, fixes lint errors and runs locks `uv.lock` to `pyproject.toml`
* `make fix-format` formats the code
* `make fix-lint` fixes linting issues
* `make fix-lint-unsafe` fixes linting issues potentially adding inadvertant bugs
* `make help` outputs the different make options
* `make install` build install the distribution
* `make install-pre-commit` installs pre-commit hooks
* `make lock` locks `uv.lock` to `pyproject.toml`
* `make install-pre-commit` installs pre-commit hooks
* `make run-tests` runs the unit tests
* `make sync` syncs the python environment with `uv.lock`

`.vscode/settings.json` is set so that unit tests can be run without further configuration.
