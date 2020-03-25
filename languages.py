from subprocess import check_output
from sys import executable

def python(filename, inputs):
    output = {}
    for input in inputs:
        output[input] = check_output([executable, filename], input=input, universal_newlines=True)
    return output

def cpp(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["g++", filename, "-g", "-O2", "-std=gnu++17", "-o", f"{problem}"])
    for input in inputs:
        output[input] = check_output([f"./{problem}"], input=input, universal_newlines=True)
    check_output(["rm", "-rf", f"{problem}"])
    return output

def c(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["gcc", filename, "-g", "-O2", "-std=gnu11", "-o", f"{problem}"])
    for input in inputs:
        output[input] = check_output([f"./{problem}"], input=input, universal_newlines=True)
    check_output(["rm", "-rf", f"{problem}"])
    return output