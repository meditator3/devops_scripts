#def is defining a function
def minmax(items):
    return min(items), max(items)
list = [83, 33, 84, 32, 85, 31, 86]
print(minmax(list)) # minmax(list) <<<tuple
#this is a tuple
lower, upper = minmax(list)
print("upper {0}".format(upper), ", lower will be:{0}".format(lower))
# more complex assigning
(a, (b, (c, d))) = (4, (3, (2,1)))
print(a, b, c, d)
a = 'jelly'
b = 'bean'
a, b = b, a # relocate assignments
print(a, b)
# also via command 'tuple' i can convert items/lists into a tuple
list2 = [561, 4, 3, 3213, 43134]
print(tuple(list2))
# can also convert tuple from strings
list3 = "Carmichael"
print(tuple(list3))
# to check if item is in a tuple
print( 5 in (3,4,2,1,5))
# or not in:
print(5 not in list2)