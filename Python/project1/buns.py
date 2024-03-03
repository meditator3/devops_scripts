# division by // zeros the float reminder, but maintain float definition if divided by float
bun = 2.40
budget = 15

print("I got " + str(int(budget//bun)) +" buns for "+ str(budget) +"$")
print("you see? this ->" + str(budget//bun) + ", is still a float")

# create same result with a loop
count = 0
buns = 0
for i in range(int(budget/bun)):
    budget = budget - bun
    count = count + 1
    print(budget, count)
print("number of buns you could by for 15$ little man:" + str(count))