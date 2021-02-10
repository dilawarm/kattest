from subprocess import check_output
import time
import os


class Language:
    def __init__(self, compile_line, run_line, remove_line):
        self.compile_line = compile_line
        self.run_line = run_line
        self.remove_line = remove_line


def run_code(filepath, inputs):
    file = os.path.join(os.getcwd(), filepath)

    filename, extension = os.path.basename(filepath).split(".")

    language_map = {
        "py": Language(None, f"python3 {file}", None),
        "cpp": Language(
            f"g++ {file} -g -O2 -std=gnu++17 -o {filename}",
            f"./{filename}",
            filename,
        ),
        "c": Language(
            f"gcc {file} -g -O2 -std=gnu11 -o {filename}", f"./{filename}", filename
        ),
        "java": Language(
            f"javac -encoding UTF-8 {file}",
            f"java -Dfile.encoding=UTF-8 -XX:+UseSerialGC -Xss64m {filename}",
            f"{filename}.class",
        ),
        "cs": Language(
            f"dmcs -optimize+ -r:System.Numerics {file}",
            f"./{filename}.exe",
            f"{filename}.exe",
        ),
        "hs": Language(
            f"ghc -dynamic -O2 {file} -o {filename}",
            f"./{filename}",
            f"{filename}.hi {filename}.o {filename}",
        ),
    }

    if extension not in language_map:
        return -1

    output = {}
    lang = language_map[extension]

    if lang.compile_line:
        check_output(lang.compile_line.split())

    start_time = time.time()

    if lang.run_line:
        for inp in inputs:
            output[inp] = check_output(
                lang.run_line.split(), input=inp, universal_newlines=True
            )

    end_time = time.time() - start_time

    if lang.remove_line:
        try:
            check_output(f"rm -rf {lang.remove_line}".split())
        except:
            try:
                check_output(
                    f"del /f {lang.remove_line}".split()
                )  # For Windows (Normie OS) users.
            except:
                pass

    return output, end_time