import sys
from kattest.script import kattest

def main():
    cmd = sys.argv[1:]
    if cmd[0] == "CF":
        kattest(cmd[1], "CF")
    elif cmd[0] == "CSES":
        kattest(cmd[1], "CSES")
    else:
        kattest(cmd[0], "Kattis")

if __name__ == "__main__":
    main()