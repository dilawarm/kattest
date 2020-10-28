import sys
from kattest.script import kattest


def main():
    cmd = sys.argv[1:]
    if cmd[0] == "CF":
        kattest(cmd[1], "CF")
    elif cmd[0] == "CSES":
        kattest(cmd[1], "CSES")
    elif cmd[0] == "Kattis":
        kattest(cmd[1], "Kattis")
    else:
        print("Wrong command :(")


if __name__ == "__main__":
    main()