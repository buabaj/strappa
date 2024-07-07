# Strappa

Strappa is a Python bootstrapper CLI tool to help set up Python projects easily and faster.

## Motivation

I was talking to my friend [Utuk](https://github.com/utukj) about why he prefers to write go more than python and he told me about how he has to put in more effort setting up a python project to enable him write good python code whereas in go, it came right out of the box. I realize this is true as most people do not even know how to set up python projects properly. This simple bootstrapper should help with that.

## Installation

You can install Strappa using pip:

```bash
pip install strappa
```

## Usage

Strappa provides a command-line interface with the following commands:

1. Set up a project in the current directory:

```bash
strappa run
```

This will:

- Set up a virtual environment
- Create a `pyproject.toml` file with pre-configured settings
- Create a `Makefile` with common development commands
- Create a `requirements.txt` file
- Set up a basic project structure (src and tests directories)
- Activate the virtual environment and install requirements

2. Execute a command in the project's virtual environment:

```bash
strappa execute <command>
```

For example:

```bash
strappa execute pip list
strappa execute python -m pytest
```

### Development Commands

This project includes a Makefile with several commands to help you develop, test, and maintain the project. Here's an overview of the available commands:

### Testing and Coverage

- `make test`: Run the project's test suite using pytest.
- `make coverage`: Run tests with coverage analysis.
- `make coverage-report`: Generate an HTML coverage report for detailed inspection.

### Linting and Formatting

- `make ruff`: Run the Ruff linter to check for code style and potential errors.
- `make ruff-fix`: Run Ruff and automatically fix issues where possible.
- `make mypy`: Run the MyPy static type checker on the source code.
- `make format`: Format the code using Ruff's formatting capabilities.
- `make lint`: Run both Ruff and MyPy for comprehensive code checking.

### Comprehensive Checks

- `make all_checks`: Run formatting, linting, and tests in sequence for a full code check.
