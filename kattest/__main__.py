import sys
from kattest.script import kattest

def main():
    try:
        filename = sys.argv[1]
        kattest(filename)
    except:
        "Could not run your code."

if __name__ == "__main__":
    main()