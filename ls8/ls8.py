#!/usr/bin/env python3

"""Main."""

from utils import *
from cpu import *

filename = get_filename()
loc = load_lines_from_file(filename)
clean_loc = parse_loc(loc)

cpu = CPU()

cpu.load(clean_loc)

cpu.run()
