parrot = "Norwegian Blue"

# prints from index 1 jumps 4 cells and prints
print(parrot[1::4])

number = "9,223;382:036 854,775;887"
# separator just are the non-number chars
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
# for every character(char placeholder) that is not seperator join it, and if it meets a seperator
# create a space between them, iterate(loop) over the whole string, until removed all seperators
# and then use split to cut them into cells.

print([int(val) for val in values])
# the [   ] for the whole arguments redfines it as an array

