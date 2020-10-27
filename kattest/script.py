from kattest.languages import run_code
from kattest.data import Kattis, CF, CSES
import emoji
import sys


def kattest(filename, site):
    """
    Method for running your code and returning output on the form {input: code output}
    Comparing user output with correct output
    """

    site_map = {"Kattis": Kattis, "CF": CF, "CSES": CSES}

    problem, extension = filename.split(".")

    if site in site_map:
        testdata = site_map[site](problem.lower())
    else:
        print("This problem site is not supported :(")
        return -1

    out = run_code(filename, problem, extension, testdata)
    if out == -1:
        print("Language is not supported :(")
        return -1
    else:
        output, time = out[0], out[1]

    counter, correct_count = 1, 0
    for out in output:
        correct = testdata[out].split("\n")
        user = output[out].split("\n")
        if formatter(user) == formatter(correct):
            print(
                f'{emoji.emojize(":white_check_mark:", use_aliases=True)} Sample Input {counter}'
            )
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
    return [out.rstrip() for out in output if out != ""]
