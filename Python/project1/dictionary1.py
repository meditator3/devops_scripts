#much like object in JS. or similar to JSON file
ages = {'ariel': 48, 'alex': 34, "bob": 29}
print(type(ages)) # will give "dict" as dictionart

# to get particular value, or key value, in JS it would be ages.ariel
print(ages['ariel']) # prints 48
print(ages['alex'])  # prints 34 

# can also add another key-value pair to the dict:
ages['kayla'] = 21
print(ages) #now added : {'ariel': 48, 'alex': 34, 'bob': 29, 'kayla': 21}

# to delete item
del ages['bob']
print(ages)

# method can work the same as list
print(ages.pop('alex')) # will remove alex but also export its value
print(ages) # {'ariel': 48, 'kayla': 21}

# to get only the key's names (not the value)
print(ages.keys()) # dict_keys(['ariel', 'kayla'])

# or just list the values
print(ages.values()) # dict_values([48, 21])

# convert dictionary into list(like convert tuple):
new_list = list(ages.values())
print(new_list) # [48, 21]

# create dictionary via this format:
weights = dict(kevin=160, bob=240, kayla=135)
print(weights) # {'kevin': 160, 'bob': 240, 'kayla': 135}

# create dictionary via tuple
# a list that contains a tuple, that we converted to dict
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors) # {'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}

# "update()" to concat dictionary to another dictionary
name_and_ages = [('alice', 32), ('bob', 48), ('charlie', 28), ('daniel', 33)]
# ^^ these are tuples inside a list
# convert to dict
d = dict(name_and_ages)
# add d to colors via update()
colors.update(d) # d is added to colors
print(colors)  # {'kevin': 'blue', 'bob': 48, 'kayla': 'red', 'alice': 32, 'charlie': 28, 'daniel': 33}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# bob is in conflict, bob was green as value, and was ran over by update , as value 48




