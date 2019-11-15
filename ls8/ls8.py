#!/usr/bin/env python3

"""Main."""

from utils import get_filename
from ls8_parser import LS8Parser
from cpu import *

filename = get_filename()

parser = LS8Parser()
parser.parse(filename)

cpu = CPU()

cpu.load(parser.lines_of_code)

cpu.run()
