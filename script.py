from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request

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
