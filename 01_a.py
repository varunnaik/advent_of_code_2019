f = open("01")
modules = f.readlines()

sum = 0
for module in modules:
    if module:
        module_weight = int(module)
        sum += (module_weight / 3) - 2


print (sum)
