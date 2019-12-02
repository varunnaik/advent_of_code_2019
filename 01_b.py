def compute_fuel(weight):
    fuel = ( weight / 3 ) - 2
    if fuel > 0:
        return fuel + compute_fuel(fuel)
    else:
        return 0

f = open("01")
modules_weights = f.readlines()

sum = 0
for weight in modules_weights:
    sum += compute_fuel(int(weight))

print(sum)
    
