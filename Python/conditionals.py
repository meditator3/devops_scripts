name = input("please enter your name: ")
age = int(input("and {0}, Your age is? :".format(name)))
print(age)

if age >= 18:
    print("it seems you are old enough to vote!")
    print("please put X in the box")
else:
    print("please come back in {0} years".format(18-age))

