#Lambda function you don't have to use def

def double(num):
    return num ** 2 # like num * num
print(double(4))

double_lambda = lambda num:num ** 2

print(double_lambda(5))

# this function does only 1 function mostly,
# one action. if we want loop or something more
# we need a regular function

# another example
full_name = lambda first, last : {first.title(), last.title()}

print(full_name("ariel", "guez"))

# example 3

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, list1))) # in normal function
# we would write if and maybe for loop







