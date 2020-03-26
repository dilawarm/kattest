from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def getTestData(problem):
    """
    Returns a dictionary on the form {input: correct output} from Kattis.
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

def CF(problem):
    """
    Returns a dictionary on the form {input: correct output} from Code Forces
    """
    num, let = problem[:-1], problem[-1]
    url = f"https://codeforces.com/problemset/problem/{num}/{let}"
    request = Request(url, headers={'User-Agent': 'Chrome Browser'})
    resp = urlopen(request)
    soup = BeautifulSoup(resp, 'html.parser')
    io = soup.find("div", class_="sample-test").text.split('\n')
    testdata = {}
    i = 0
    while i != len(io) - 1:
        if io[i] == "Input":
            input = ""
            i += 1
            while io[i] != "Output":
                input += io[i] + '\n'
                i += 1
            output = ""
            i += 1
            while io[i] != "Input":
                if i == len(io) - 1:
                    break
                output += io[i] + '\n'
                i += 1
            testdata[input] = output
    return testdata