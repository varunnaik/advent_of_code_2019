f = open("02")
instructions = map(int, str.split(f.read().strip(), ","))

for n in xrange(0, len(instructions), 4):
    instruction = instructions[n]
    if instruction == 99:
        print (instructions[0])
        exit()
    n1 = instructions[instructions[n + 1]]
    n2 = instructions[instructions[n + 2]]
    if instruction == 1:
        instructions[instructions[n + 3]] = n1 + n2
    elif instruction == 2:
        instructions[instructions[n + 3]] = n1 * n2
    else:
        raise("Unknown instruction")





