# tuple is a "closed array", cannot add values or change
a = (1.0, 2.0, 3.0)
print(a)
# if we want to add values to tuple we can define new tuple and add the previous
point_3d = a + (4.0, 5.0)
print(point_3d)
point_3d = a # redeclaration is fine in python
print(point_3d)
x, y, z = point_3d # there must be corresponding number of variables to match tuple
print(x,y,z) # this method of putting variables from tuple, called "unpacking"
#tuple can be string and numbers too
t= ('norway', 5.323, 4)
print(t)
# like array it has index
print(t[0], t[1], t[2])
# length of tuple
print("length of t tuple: {0}".format(len(t)))
# 2d tuple is also possible, or "nested tuple"
a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))
print(a[2]) # (2620, 2924)
print(a[2][1]) # 2924
# example of difference between tuple and number
h = (391)
print(type(h)) # int
k = (391,)
print(type(k)) # tuple
# this below is like assigning type before assigning values
e = ()
print(type(e)) # tuple!
# this is also a tuple:
p = 1, 1, 1, 6, 19
print(p)
print(type(p))