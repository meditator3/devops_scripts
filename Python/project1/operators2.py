# and
# and will return first value which is false in the chain
print(0 and 1) # 0. because 0 is false-0 is not  a value
print(1 and 2) # 2. because he will prefer the last one in the chain
print(1 and 7) #7. same reason
# this is oppoiste of "or"

print( 1 == 1 and print("something")) # something. because first value is true.
print( 1 == 2 and print("something")) # false. because first value is true.
