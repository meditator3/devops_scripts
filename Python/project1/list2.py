my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list1 = ['a', 2, 3, 4, 5]
my_list1.append(6) # adds 6 to the list
my_list1.append(7) # adds 7 to the list
my_list2 = my_list1 + [8, 9, 10]
print(my_list2)
my_list1 += [8, 9, 10] # appends this array to my_list1 array
print(my_list1)
#change values inside the array(does not include last value. range is until 2:
my_list1[1:3] = ['b', 'c']
print(my_list1)
# wrong. it includes range 3. just that if you don't put value, it won't replace
my_list1[3:5] = ['d', 'e', 'f'] # so this adds 'f' as well!
print(my_list1)
# remove value from array
my_list1.remove('b') #the order has changed probably
print(my_list1)

my_list1.pop() #removes last item from the last
print(my_list1)
