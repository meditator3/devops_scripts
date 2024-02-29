colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color) # prints all colors

print("=======")
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color) # green
print("=======")
ages = {'kevin':59, 'bob':40, 'kayla':21}
for key in ages:
    print(key) # will print the names only

# unpacking with for loop

list_of_points = [(1, 2), (2, 3), (3, 4)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")
# this ^^ will print x:1, y:2 etc..
