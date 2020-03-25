from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request
from languages import python, cpp, c
import emoji

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
    """
    problem, extension = filename.split(".")
    testdata = getTestData(problem)
    if extension == "py":
        output = python(filename, testdata)
    elif extension == "cpp":
        output = cpp(filename, testdata)
    elif extension == "c":
        output = c(filename, testdata)
    else:
        return "Language is not supported :("
    counter = 1
    for out in output:
        if output[out] == testdata[out]:
            print(f'{emoji.emojize(":white_check_mark:", use_aliases=True)} Sample Input {counter}')
        else:
            print(f'{emoji.emojize(":x:")} Sample Input {counter}')
        print("INPUT")
        print(out)
        print("CORRECT OUTPUT")
        print(testdata[out])
        print("USER OUTPUT")
        print(output[out])
        counter += 1

