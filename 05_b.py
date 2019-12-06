from enum import Enum

class Opcodes(Enum):
    add = 1
    multiply = 2
    store = 3
    output = 4
    jump_if_true = 5
    jump_if_false = 6
    less_than = 7
    equals = 8
    quit = 99

class Parametermodes(Enum):
    immediate = 1
    position = 0

opcode_data = {
    Opcodes.add: {
        "parameters": 3
    },
    Opcodes.multiply: {
        "parameters": 3
    },
    Opcodes.store: {
        "parameters": 1
    },
    Opcodes.output: {
        "parameters": 1
    },
    Opcodes.quit: {
        "parameters": 0
    },
    Opcodes.jump_if_true: {
        "parameters": 2
    },
    Opcodes.jump_if_false: {
        "parameters": 2
    },
    Opcodes.less_than: {
        "parameters": 3
    },
    Opcodes.equals: {
        "parameters": 3
    }
}
    
def process_intcode(intcode):
    n = 0
    while True:
        opcode, parameters = parse_opcode(intcode[n])
        if opcode == Opcodes.quit:
            return intcode
        elif opcode == Opcodes.store:
            value = int(input('Input:'))
            store_parameter_value(value, n+1, intcode)
        elif opcode == Opcodes.output:
            print (read_parameter_value(n+1, intcode))
        elif opcode == Opcodes.add:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            store_parameter_value(v1 + v2, n + 3, intcode, parameters.pop())
        elif opcode == Opcodes.multiply:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            store_parameter_value(v1 * v2, n + 3, intcode, parameters.pop())
        elif opcode == Opcodes.jump_if_true:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            if v1 != 0:
                n = v2
                continue
        elif opcode == Opcodes.jump_if_false:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            if v1 == 0:
                n = v2
                continue
        elif opcode == Opcodes.less_than:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            result = int(v1 < v2)
            store_parameter_value(result, n + 3, intcode, parameters.pop())
        elif opcode == Opcodes.equals:
            v1 = read_parameter_value(n+1, intcode, parameters.pop())
            v2 = read_parameter_value(n+2, intcode, parameters.pop())
            result = int(v1 == v2)
            store_parameter_value(result, n + 3, intcode, parameters.pop())
        else:
            print(opcode, Opcodes(opcode))
            raise "Unknown instruction"

        n+= opcode_data[opcode]["parameters"] + 1

def parse_opcode(intcode):
    instruction = str(intcode)
    opcode = Opcodes(int(instruction[-2:]))
    num_parameters = opcode_data[opcode]["parameters"]
    # The following line returns a list of int param types, the list may be empty
    paramcodes = list(map(int, list(instruction[:-2])))
    # Convert these to Parametermodes enums, enough for the opcode, using defaults if necessary
    parameters = [Parametermodes(x) for x in paramcodes]
    parameters = [Parametermodes.position] * (num_parameters - len(parameters)) + parameters

    return opcode, parameters

def read_parameter_value(position, intcode, mode=Parametermodes.position):
    mode = Parametermodes(mode)
    if mode == Parametermodes.immediate:
        return intcode[position]
    elif mode == Parametermodes.position:
        return intcode[intcode[position]]
    else: raise "Unknown parameter mode"

def store_parameter_value(value, position, intcode, mode=Parametermodes.position):
    mode = Parametermodes(mode)
    if mode == Parametermodes.immediate:
        intcode[position] = value
    elif mode == Parametermodes.position:
        intcode[intcode[position]] = value
    else: raise "Unknown parameter mode"

f = open("05")
inputs = list(map(int, str.split(f.read().strip(), ",")))

result = process_intcode(inputs)
#print(result)
