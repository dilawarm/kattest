from subprocess import check_output
from sys import executable
import time

def python(filename, inputs):
    output = {}
    startTime = time.time()
    for input in inputs:
        output[input] = check_output([executable, filename], input=input, universal_newlines=True)
    endTime = time.time() - startTime
    return output, endTime

def cpp(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["g++", filename, "-g", "-O2", "-std=gnu++17", "-o", f"{problem}"])
    startTime = time.time()
    for input in inputs:
        output[input] = check_output([f"./{problem}"], input=input, universal_newlines=True)
    endTime = time.time() - startTime
    try:
        check_output(["rm", "-rf", f"{problem}"])
    except:
        pass
    return output, endTime

def c(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["gcc", filename, "-g", "-O2", "-std=gnu11", "-o", f"{problem}"])
    startTime = time.time()
    for input in inputs:
        output[input] = check_output([f"./{problem}"], input=input, universal_newlines=True)
    endTime = time.time() - startTime
    try:
        check_output(["rm", "-rf", f"{problem}"])
    except:
        pass
    return output, endTime

def java(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["javac", "-encoding", "UTF-8", filename])
    startTime = time.time()
    for input in inputs:
        output[input] = check_output(["java", "-Dfile.encoding=UTF-8", "-XX:+UseSerialGC", "-Xss64m", f"{problem}"], 
                                      input=input, universal_newlines=True)
    endTime = time.time() - startTime
    try:
        check_output(["rm", "-rf", f"{problem}.class"])
    except:
        pass
    return output, endTime

def cSharp(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["dmcs", "-optimize+", "-r:System.Numerics", filename])
    startTime = time.time()
    for input in inputs:
        output[input] = check_output([f"./{problem}.exe"], input=input, universal_newlines=True)
    endTime = time.time() - startTime
    try:
        check_output(["rm", "-rf", f"{problem}.exe"])
    except:
        pass
    return output, endTime

def haskell(filename, inputs):
    output = {}
    problem = filename.split(".")[0]
    check_output(["ghc", "-dynamic", "-O2", filename, "-o", problem])
    startTime = time.time()
    for input in inputs:
        output[input] = check_output([f"./{problem}"], input=input, universal_newlines=True)
    endTime = time.time() - startTime
    try:
        check_output(["rm", "-rf", f"{problem}.hi", f"{problem}.o", f"{problem}"])
    except:
        pass
    return output, endTime
