# looping over dictionary
colors = dict(aquamarine='#7FFFD4', burlywood='#DEB887')
print(colors) # {'aquamarine': '#7FFFD4', 'burlywood': '#DEB887'}

for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key]))

# explanation: once assigning a name in the template listerals, we must define it in
# .format also

# loop over values:
for value in colors.values():
    print(value)
# #7FFFD4
# #DEB887

#loop over keys without values
for key in colors.keys():
    print(key)
# aquamarine
# burlywood

# iterate over both, like the first example
for key, value in colors.items():
    print("{key} => {value}".format(key=key, value=value))




