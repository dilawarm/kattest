import sys
from kattest.script import kattest

def main():
    try:
        cmd = sys.argv[1:]
        if cmd[0] == 'CF':
            kattest(cmd[1], False)
        else:
            kattest(cmd[0], True)
    except:
        print("Could not run your code.")
        
if __name__ == "__main__":
    main()