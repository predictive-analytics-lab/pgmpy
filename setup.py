#!/usr/bin/env python3

from setuptools import setup, find_packages

VERSION = "v0.1.8"

setup(
    name="pgmpy",
    version=VERSION,
    description="A library for Probabilistic Graphical Models",
    packages=find_packages(exclude=["tests"]),
    author="Ankur Ankan",
    author_email="ankurankan@gmail.com",
    url="https://github.com/pgmpy/pgmpy",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Topic :: Scientific/Engineering",
    ],
    long_description="https://github.com/pgmpy/pgmpy/blob/dev/README.md",
    install_requires=[
        "networkx >= 2.3",
        "numpy >= 1.17.2",
        "scipy >= 1.3.1",
        "pandas >= 0.25",
        "pyparsing >= 2.4.2",
        "statsmodels >= 0.10.1",
        "tqdm >= 4.36.1",
        "joblib >= 0.14",
        "numba >= 0.46",
    ],
    extras_require={
        "dev": [
            "black",
            "mypy >= 0.720",
            "pre-commit",
            "pylint >= 2.0",
            "pytest >= 3.3.2",
            "pytest-cov >= 2.6.0",
            "mock",
            "nose",
        ]
    },
)
