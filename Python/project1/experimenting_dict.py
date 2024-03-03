ages = {'ariel': 48, 'alex': 34, "bob": 29}
print(type(ages)) # will give "dict" as dictionart

# to get particular value, or key value, in JS it would be ages.ariel
print(ages['ariel'])
print(ages['alex'])
print(ages.values())
new_list = list(ages.values())
print(new_list)
print(ages.keys())
print("converted to list", list(ages.keys()))