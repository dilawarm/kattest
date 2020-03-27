# kattest
Script for testing your code with the sample data files provided by Kattis, Code Forces and CSES!

## Requirements
* Python 3.6 or above.
* Compilers for the different languages you want to use with _kattest_. Check out [Kattis](https://open.kattis.com/help) for more.

## Supported languages
* C
* C++
* Java
* Python 3

## How to install
On Ubuntu / Mint, install <i>kattest</i> with the following commands:
```
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
sudo pip3 install kattest
```
On other systems, install <i>kattest</i> by using `pip`:
```
pip install kattest
```

## How to run
### Kattis
Run the following command from the same directory as your solution:
```
kattest [Problem ID].[extension]
Example: kattest exponial.cpp
```

### Code Forces
Run the following command from the same directory as your solution:
```
kattest CF [Problem ID].[extension]
Example: kattest CF 1328A.py
```

### CSES
Run the following command from the same directory as your solution:
```
kattest CSES [Problem ID].[extension]
Example: kattest CSES 1091.c
```
Enjoy!
