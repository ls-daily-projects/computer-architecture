"""CPU functionality."""

import sys


def ldi(ram, pc, register):
    value = ram[pc + 1]
    register[value] = ram[pc + 2]
    return 2


def prn(ram, pc, register):
    register_location = ram[pc + 1]
    register_value = register[register_location]
    print(register_value)
    return 1


def halt(ram, pc, register):
    sys.exit(0)
    return 0


def mult(ram, pc, register):
    num_1_location = ram[pc + 1]
    num_2_location = ram[pc + 2]
    num_1 = register[num_1_location]
    num_2 = register[num_2_location]
    print(num_1 * num_2)
    return 2


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0b0] * 8
        self.ram = [0b0] * 0xFF
        self.pc = 0
        self.mar = None  # holds address currently being read or written
        self.mdr = None  # holds value to write or value just read
        self.dispatch_table = {}
        self.setup_instructions()

    def setup_instructions(self):
        self.dispatch_table[0b10000010] = ldi
        self.dispatch_table[0b01000111] = prn
        self.dispatch_table[0b00000001] = halt
        self.dispatch_table[0b10100010] = mult

    def load(self, program=[]):
        """Load a program into memory."""

        address = 0

        program = [int(line, 2) for line in program]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ram_read(self, address):
        """Takes an address and returns the corresponding value in MAR"""
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value
        return self

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.pc < len(self.ram):
            self.mar = self.ram_read(self.pc)

            if self.mar in self.dispatch_table:
                self.mdr = self.dispatch_table[self.mar]
                pc_delta = self.mdr(self.ram, self.pc, self.reg)
                self.pc += pc_delta
                continue

            self.pc += 1
