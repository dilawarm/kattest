from kattest.languages import python, cpp, c, java, cSharp
from kattest.data import Kattis, CF, CSES
import emoji
import sys

def kattest(filename, site):
    """
    Method for running your code and returning output on the form {input: code output}
    Comparing user output with correct output
    """
    problem, extension = filename.split(".")
    if site == "Kattis":
        testdata = Kattis(problem.lower())
    elif site == "CF":
        testdata = CF(problem.lower())
    elif site == "CSES":
        testdata = CSES(problem.lower())
    if extension == "py":
        output, time = python(filename, testdata)
    elif extension == "cpp":
        output, time = cpp(filename, testdata)
    elif extension == "c":
        output, time = c(filename, testdata)
    elif extension == "java":
        output, time = java(filename, testdata)
    elif extension == "cs":
        output, time = cSharp(filename, testdata)
    else:
        print("Language is not supported :(")
        return -1
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