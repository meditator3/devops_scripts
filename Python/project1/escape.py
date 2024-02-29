splitString = "This String has been\nsplit over \nseveral \nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# we have put \ near the "'" so that the script will know
# to ignore it, so it won't close the string sentence
print('the pet shop owner said "NO, no, \'e\'s uh,...he\'s resting".')

# here we put escape \ for the apstrophy near the "NO and also at the end
print('the pet shop owner said \"NO, no, \'e\'s uh,...he\'s resting\".')

# here we just put 3 apostrophies in the start and end of string
# and it will ignore anything inside the string
print(""""the pet shop owner said \"NO, no, \'e\'s uh,...he\'s resting\".""")
# to print things in a single line in a loop
for i in range(1, 6):
    print(i, end=' ')  # Use a space (' ') as the end parameter value to separate the items with a space

# Output: 1 2 3 4 5

# this has the same effect as \n
anothersplitstring = """this string has been
split over
several
lines
"""

print(anothersplitstring)