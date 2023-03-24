The first commit in this repo (app, README, demo) was written by GPT-4. Screenshots of that conversation are [here](./gpt4-conversation.md). The prompt was

```
# Task
Write a command line application in Python called autopoilot that repeatedly
tries to build and test some code; each time the build or tests fail it sends
the code and error output to an AI API requesting a modified version of the code
that fixes the error.

# User contract
- autopilot must be run from a directory containing executable files named 'build' and 'test'.
- We will call this directory the "project root". It must be the root of git repository.
- autopilot receives one positional argument which is the path to the file it will modify, relative to the project root
- The API key must be stored in an env var named OPENAI_API_KEY

# Application requirements
- When the build or test stage fails, the current version of the file must be committed, together with the stderr
- Use the openai client.
- Create a setup.py with a command line entrypoint
- Create a README.md

Your output should consist only of code blocks specifying the required file
contents, together with the file names.

Create all the files necessary for a demo of the usage of autopilot. The code
should be fixed by autopilot after 2 or 3 iterations.
```

---

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
