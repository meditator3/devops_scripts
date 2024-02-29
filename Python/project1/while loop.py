#this will print infinite loop

#while True:
 #   print("Looping")
count = 1
while count <= 4:
    print("looping")
    count += 1 # count+1 each loop

# prints 4 times "looping"
count = 0
while count <= 20: # prints only odd numbers until 20
    if count % 2 == 0: # if count is even
        count += 1
        continue
    print (f"We're count odd number: {count}") # shortcut for .format
    count += 1

#demonstrates "break"
count = 0
while count <= 20:
    if count % 2 == 0:  # if count is even
       break
print("out of loop")
