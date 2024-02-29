"""
	Write a program which will find all such numbers which are divisible by 7
	but are not a multiple of 5,
	between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a single line.

"""

num_arr = [] # defines an array of wanted numbers to be represented in single line
for num in range(2000, 3201):
    if (num % 7 == 0) and (num % 5 != 0):
        num_arr.append(num) # appends correct number into the array

output_without_brackets = str(num_arr)[1:-1] # removes the [ and ] by starting on index 1 and ending on -1

print(output_without_brackets)
