from enum import Enum

class Opcodes(Enum):
    add = 1
    multiply = 2
    quit = 99

def process_intcode(intcode):
    n = 0
    while True:
        opcode = intcode[n]

        if Opcodes(opcode) == Opcodes.quit:
            return intcode

        if Opcodes(opcode) == Opcodes.add:
            n1 = intcode[intcode[n + 1]]
            n2 = intcode[intcode[n + 2]]
            intcode[intcode[n + 3]] = n1 + n2
            n += 4
        elif Opcodes(opcode) == Opcodes.multiply:
            n1 = intcode[intcode[n + 1]]
            n2 = intcode[intcode[n + 2]]
            intcode[intcode[n + 3]] = n1 * n2
            n += 4
        else:
            print(opcode, Opcodes(opcode))
            raise "Unknown instruction"

f = open("02")
inputs = list(map(int, str.split(f.read().strip(), ",")))

for i in range(0,100):
    for j in range(0,100):
        intcode_copy = inputs.copy()
        intcode_copy[1] = i
        intcode_copy[2] = j
        
        try:
            result = process_intcode(intcode_copy)
        except:
            print("Exception")
            continue
        if result[0] == 19690720:
            print (100 * result[1] + result[2])
            exit()
