from setuptools import setup, find_packages

setup(
    name="autopilot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "autopilot = autopilot.autopilot:main",
        ],
    },
)
