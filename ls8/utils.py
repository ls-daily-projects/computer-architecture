import sys


def parse_loc(lines):
    clean_loc = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        if "#" in line:
            line = line.split("#")[0]

        clean_loc.append(line)

    return clean_loc


def load_lines_from_file(filename):
    lines = []

    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
    return lines


def get_filename():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: ls8.py <path-to-ls8-file>")
        sys.exit(1)
    return sys.argv[1]
