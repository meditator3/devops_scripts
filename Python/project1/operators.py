# not operator:
name = ""
if not name: # true
    print("no name given")

# or operator
first = ""
last = "Thompson"
if first or last:
    print("The use has First name or Last name")
last = ""

# assigning value without if condition
last_name = last or "Doe"
print(last_name) # Doe

# default perferences of or, he will prefer first value or any value of the first-first
print(0 or 1) # 1
print(1 or 2) # 1 because first value is first
print(2 or 7) # 2, same reason
print(0 or 7) # 7 because only 7 is value, 0 is not.
print(1 or 7) # 1 because it has value first

#example of or assigning inside variable
last = "ariel"
last_name = last or "Doe"
print(last_name) # ariel, because has value first

