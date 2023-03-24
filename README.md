# autopilot

A command-line application in Python that repeatedly tries to build and test code. When the build or tests fail, it sends the code and error output to an AI API to request a modified version of the code that fixes the error.

## User contract

- autopilot must be run from a directory containing executable files named 'build' and 'test'.
- The directory must be the root of a git repository.
- autopilot receives one positional argument: the path to the file it will modify, relative to the project root.
- The API key must be stored in an environment variable named OPENAI_API_KEY.

## Installation

1. Install the autopilot package:

```bash
pip install .
```

2. Set the OPENAI_API_KEY environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key
```

## Usage

In the project root directory, run autopilot with the path to the code file you want to modify:

```
autopilot path/to/code_file.py
```

## Requirements

Python 3.6+
openai Python library

## How it works

autopilot continuously builds and tests your code using the 'build' and 'test' executables. When a failure occurs, it sends the code and error output to the AI API, updates the code with the fixed version provided by the API, retries the build and tests, and commits the changes with the error output as the commit message.

## License

MIT
