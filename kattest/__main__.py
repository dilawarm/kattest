from kattest.script import kattest
import argparse


def main():
    parser = argparse.ArgumentParser(description="Test your solution with kattest")
    parser.add_argument(
        "-s", "--site", type=str, metavar="", required=True, help="problem site"
    )
    parser.add_argument(
        "-p", "--problem", type=str, metavar="", required=True, help="problem ID"
    )
    parser.add_argument(
        "-f", "--file", type=str, metavar="", required=True, help="filename"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    args = parser.parse_args()

    kattest(args)


if __name__ == "__main__":
    main()