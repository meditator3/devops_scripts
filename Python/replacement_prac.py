# we cant print strings and numbers so we use str() to convert numbers to strings
age = 24*2
print("My age is " +str(age) + " Years")

print("My age is {0} years".format(age)) # this {0} template literals

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

for i in range(1, 13):
    print("No, {0} squared is {1} and cubed is {2}".format(i, i**2, i**3)) # prints values of squared cubed of i
    print()
    print("No, {0:2} squared is {1:3} and cubed is {2}".format(i, i**2, i**3)) # prints the same thing but with space bars according to :number
# the :2, or :3 means how many spacebars per template literals
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) # because its not an array, MTWTFSS
