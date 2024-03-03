if True:
    print("was True") # was true, cause true is true

if False:
    print("was True") # no print! because it checks false, and false doesn't
    # happen

if False:
    print("was True")
else:
    print("was False")
# prints false beacuse it relates zeros on to the false in the if condition, even though its true that it is false.

name = "kevin"
#else if = elif
if len(name) >=6:
    print("name is long")
elif len(name) == 5:
    print("name is 5 characters")
elif len(name) >= 4:
    print("name is 4 characters or more")
else:
    print("name is short")

