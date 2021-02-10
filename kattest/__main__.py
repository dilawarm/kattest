from kattest.script import kattest
import argparse


def main():
    parser = argparse.ArgumentParser(description="Test your solution with kattest")
    parser.add_argument(
        "-s",
        "--site",
        type=str,
        metavar="",
        required=True,
        help="problem site [Kattis, CSES, CF]",
    )
    parser.add_argument(
        "-p", "--problem", type=str, metavar="", required=True, help="problem ID"
    )
    parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        metavar="",
        required=True,
        help="path to your solution",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    args = parser.parse_args()

    kattest(args)


if __name__ == "__main__":
    main()