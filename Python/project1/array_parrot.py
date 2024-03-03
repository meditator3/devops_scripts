parrot = "Norwegian Blue"

# prints from index 1 jumps 4 cells and prints
print(parrot[1::4])

number = "9,223;382:036 854,775;887"
# separator just are the non-number chars
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


