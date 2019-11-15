import sys


def get_filename():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: ls8.py <path-to-ls8-file>")
        sys.exit(1)
    return sys.argv[1]
