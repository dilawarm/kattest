from kattest.languages import python, cpp, c, java
from kattest.data import getTestData, CF
import emoji
import sys

def kattest(filename, kattis):
    """
    Method for running your code and returning output on the form {input: code output}
    Comparing user output with correct output
    """
    problem, extension = filename.split(".")
    if kattis:
        testdata = getTestData(problem.lower())
    else:
        testdata = CF(problem)
    if extension == "py":
        output, time = python(filename, testdata)
    elif extension == "cpp":
        output, time = cpp(filename, testdata)
    elif extension == "c":
        output, time = c(filename, testdata)
    elif extension == "java":
        output, time = java(filename, testdata)
    else:
        return "Language is not supported :("
    counter, correct_count = 1, 0
    for out in output:
        correct = testdata[out].split("\n")
        user = output[out].split("\n")
        if formatter(user) == formatter(correct):
            print(f'{emoji.emojize(":white_check_mark:", use_aliases=True)} Sample Input {counter}')
            correct_count += 1
        else:
            print(f'{emoji.emojize(":x:", use_aliases=True)} Sample Input {counter}')
        print("INPUT")
        print(out)
        print("CORRECT OUTPUT")
        print(testdata[out])
        print("USER OUTPUT")
        print(output[out])
        print("------------------------------")
        counter += 1
    print(f"Time: {time} seconds")
    print(f"Verdict: {correct_count}/{counter-1} correct cases")

def formatter(output):
    return [out.rstrip() for out in output if out != '']

kattest("1328D.cpp", False)