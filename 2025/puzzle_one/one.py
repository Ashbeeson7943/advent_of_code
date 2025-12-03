
from helpers import read_file

class Dial():
    def __init__(self, dial_size, initial_value):
        self.current_index = initial_value
        self.dial_size = dial_size
        self.dial = self.create_dial()

    def __repr__(self):
        return f"Dial is at: {self.read_dial()}"

    def create_dial(self):
        d = []
        for i in range(0, self.dial_size):
            d.append(i)
        return d
    
    def move_dial(self, move_amount):
        self.current_index = (self.current_index + move_amount) % len(self.dial)

    def read_dial(self):
        return self.dial[self.current_index]

def solve(raw_instructions_filename, verbose = False):
    inputs = read_file(raw_instructions_filename)
    
    dial = Dial(100, 50)
    zero_count = 0
    rotations = 0

    instructions = extract_instructions(inputs)

    for instruction in instructions:
        dial.move_dial(instruction)
        if dial.read_dial() ==  0:
            zero_count += 1

    if verbose:
        print(f"Password = {zero_count}")
        print(f"Updated Password = {zero_count + rotations}")

def extract_instructions(input):
    iterable_instructions = input.split("\n")
    decoded_instructions = []
    for instruction in iterable_instructions:
        sign = instruction[:1]
        value = int(instruction[1:])
        if sign == "L":
            decoded_instructions.append(value * -1)
        else:
            decoded_instructions.append(value * 1)
    return decoded_instructions