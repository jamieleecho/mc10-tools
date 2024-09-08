#!/usr/bin/env python3

import setuptools

# VERSION MUST be defined on line 6
VERSION = "0.8"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mc10-tools",
    version=VERSION,
    author="Jamie Cho",
    author_email="jamieleecho+mc10-tools@gmail.com",
    description="Set of MC-10 tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamieleecho/mc10-tools",
    packages=setuptools.find_packages(where="."),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click >= 7.1.2",
        "ply >= 3.11",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "c10tobas=mc10.c10tobas:c10tobas",
            "bastoc10=mc10.bastoc10:bastoc10",
        ],
    },
)
