def print_even(test_string):
    for i in test_string:
        if i=="demo":
            print(i)
            yield i


demo_string="This is demo string,\ This is demo string, This is demo string"
count = 0
print("The number of demo in string is : ", end="")
demo_string=demo_string.split()
for j in print_even(demo_string):
    count=count+1
    print(count)