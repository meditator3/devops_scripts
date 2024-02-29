def nextSquare():
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# yield returns the value of the function- but doesn't
# stop the function, it retains the value.
# but it doesnt save all the states
# just the one that is called upon, thus saving memory(maybe)
# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)


