#!/usr/bin/env python
# encoding: UTF-8

import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)


long_description = "Script for testing your code with the sample data files provided by Kattis, Code Forces and CSES!"

setup(
    name="kattest",
    version="1.7",
    description="Script for testing your code with the sample data files provided by Kattis, Code Forces and CSES!",
    url="https://github.com/dilawarm/kattest",
    license="MIT",
    long_description=long_description,
    author_email="dilawarmm@outlook.com",
    author="Dilawar Mahmood",
    packages=find_packages(),
    download_url="https://github.com/dilawarm/kattest/archive/v1.7.tar.gz",
    install_requires=[
        "emoji",
        "beautifulsoup4",
    ],
    entry_points={"console_scripts": ["kattest = kattest.__main__:main"]},
    cmdclass={"install": install},
)