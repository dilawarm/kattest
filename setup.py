import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)


long_description = ""

try:
    if os.path.isfile("README.rst"):
        long_description = open("README.rst", "r").read()
    elif os.path.isfile("README.md"):
        long_description = open("README.md", "r").read()
except Exception as error:
    print("Unable to read the README file: " + str(error))

setup(
    name="kattest",
    version="0.1",
    description="Script for testing your code with the sample data files provided by Kattis.",
    url="https://github.com/dilawarm/kattest",
    license="MIT",
    long_description=long_description,
    author_email="dilawarmm@outlook.com",
    author="Dilawar Mahmood",
    packages=find_packages(),
    download_url = "https://github.com/dilawarm/kattest/archive/v_01.tar.gz",
    install_requires=[
        'emoji',
    ],
    entry_points={
        "console_scripts": [
            "kattest = kattest.__main__:main"
        ]
    },
    cmdclass={"install": install}
)
