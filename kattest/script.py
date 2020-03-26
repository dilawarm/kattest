from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request
from kattest.languages import python, cpp, c, java
import emoji
import sys

def getTestData(problem):
    """
    Returns a dictionary on the form {input: correct output}
    """
    url = f"https://open.kattis.com/problems/{problem}/file/statement/samples.zip"
    request = Request(url, headers={'User-Agent': 'Chrome Browser'})
    resp = urlopen(request)
    zipfile = ZipFile(BytesIO(resp.read()))
    data = ["".join([line.decode("UTF-8") for line in zipfile.open(name).readlines()]) for name in zipfile.namelist()]
    testdata = {}
    for i in range(0, len(data), 2):
        if i < len(data) - 1:
            testdata[data[i]] = data[i + 1]
    return testdata

def kattest(filename):
    """
    Method for running your code and returning output on the form {input: code output}
    Comparing user output with correct output
    """
    problem, extension = filename.split(".")
    testdata = getTestData(problem.lower())
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
    return [out.rstrip() for out in output]