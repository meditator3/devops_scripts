import sys # to accept paramters i need this library
print(f"first argument: {sys.argv[0]}")
#this ^^ prints the path: K:\DevOps\Python\project1\argument_passing.py
# because index [0] in argv leads to the path and not the argument passed afterwards
# now we have to create an argument in command line
# in cmd: >python argument_passing.py ariel
# the added argument, "ariel" was added in argv[1] < index 1 will now read the argument passed
# or else we would get error for no argument in index 1

print(f"second argument: {sys.argv[1]}")
# or we can just ask for both of them using [0:] , which means till the end
print(f"positional argument: {sys.argv[0:]}")
# then we can write in cmd : python argument_passing.py ariel guez
# it will print [argument_passing.py, ariel, guez] as a list
# also the name of the arguments now is "positional"
