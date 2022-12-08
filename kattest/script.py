from kattest.languages import run_code
from kattest.data import Kattis, CF, CSES
import emoji


def kattest(args):
    """
    Method for running your code and returning output on the form {input: code output}
    Comparing user output with correct output
    """

    site_map = {"Kattis": Kattis, "CF": CF, "CSES": CSES}

    problem = args.problem
    filepath = args.filepath
    site = args.site
    quiet = args.quiet

    if site in site_map:
        testdata = site_map[site](problem.lower())
    else:
        print("This problem site is not supported :(")
        return -1

    out = run_code(filepath, testdata)
    if out == -1:
        print("Something went wrong :(")
        return -1
    else:
        output, time = out[0], out[1]

    counter, correct_count = 0, 0
    for out in output:
        correct = testdata[out].split("\n")
        user = output[out].split("\n")
        if formatter(user) == formatter(correct):
            if not quiet:
                print(
                    f'{emoji.emojize(":white_check_mark:", language="alias")} Sample Input {counter}'
                )
            correct_count += 1
        else:
            if not quiet:
                print(
                    f'{emoji.emojize(":x:", language="alias")} Sample Input {counter}'
                )
        if not quiet:
            print("INPUT")
            print(out)
            print("CORRECT OUTPUT")
            print(testdata[out])
            print("USER OUTPUT")
            print(output[out])
            print("------------------------------")
        counter += 1
    print(f"Time: {time} seconds")
    print(f"Verdict: {correct_count}/{counter} correct cases")


def formatter(output):
    return [out.rstrip() for out in output if out != ""]