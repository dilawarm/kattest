from subprocess import check_output
from sys import executable
import time


class Language:
    def __init__(self, compile_line, run_line, remove_line):
        self.compile_line = compile_line
        self.run_line = run_line
        self.remove_line = remove_line


def run_code(filename, problem, extension, inputs):

    language_map = {
        "py": Language(None, f"python3 {filename}", None),
        "cpp": Language(
            f"g++ {filename} -g -O2 -std=gnu++17 -o {problem}",
            f"./{problem}",
            problem,
        ),
        "c": Language(
            f"gcc {filename} -g -O2 -std=gnu11 -o {problem}", f"./{problem}", problem
        ),
        "java": Language(
            f"javac -encoding UTF-8 {filename}",
            f"java -Dfile.encoding=UTF-8 -XX:+UseSerialGC -Xss64m {problem}",
            f"{problem}.class",
        ),
        "cs": Language(
            f"dmcs -optimize+ -r:System.Numerics {filename}",
            f"./{problem}.exe",
            f"{problem}.exe",
        ),
        "hs": Language(
            f"ghc -dynamic -O2 f{filename} -o f{problem}",
            f"./{problem}",
            f"{problem}.hi {problem}.o, {problem}",
        ),
    }

    if extension not in language_map:
        return -1

    output = {}
    lang = language_map[extension]

    if lang.compile_line:
        check_output(lang.compile_line.split())

    start_time = time.time()

    for inp in inputs:
        output[inp] = check_output(
            lang.run_line.split(), input=inp, universal_newlines=True
        )

    end_time = time.time() - start_time

    try:
        check_output(f"rm -rf {lang.remove_line}".split())
    except:
        pass

    return output, end_time
