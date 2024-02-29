parrot  = "Norwegian Blue"

print (parrot) # norwe....etc
print(parrot[3]) #   w

print(parrot[-1]) # starts from the end, brings "e"
print(parrot[0:6]) # Norweg 0-5 range
print(parrot[:9]) # same 0-9: "Norwegian"
print(parrot[10:]) # blue
print(parrot[:]) # Norwegian Blue

print(parrot[0:6:2]) # jumps 2 (or 1 distance) between 0-6: "Nre"

number = "9,223;372:036 854,775;807"
seperators = number[1::4] # discovered pattern of commas and seprators ; :
print(seperators) # ,;: ,;
# join got all numbers togethar separated by space bar, and split made it an array
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1] # drives backwards because of -1 in the range
print(backwards)