# reading from JSON
#( this creates a directory called processed, and goes over each file it accepted
# and move it to that directory
# so we need to calculate the permissions)
# we go over all the reciepts  from JSON
# then we TOTAL the values of the reciepts
# move it into the folder processed.
# the files of the reciepts are read from new folder. 

# now we won't put shebang bin bash, but run it in bash via python <filename>
import glob # this lib searches for a path name we defined, and returns the files list
import os # to create the folder
import shutil
import json

try:
   os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

receipts = glob.glob('./new/receipt-[0-9]*.json') # this shows all files with .json on this path we defined
print(receipts)

subtotal = 0.0 # float as we know
for path in receipts:
    with open(path) as f:
        content = json.load(f) # json.load is special function that i load the content of json into "content", f is what
        #print(content) # we iterate over the paths
        subtotal += float(content['receipt']['purchasedItems'][0]['price']) # [0] because the price is inside an array
        # also this [<name>][<name>] etc is to access nested JSON elements
        #print(subtotal)
    name = path.split('/')[-1] # this will bring only the name of the file, without the path, -1 starts at the end of string
    destination = f"./processed/{name}" # this will use template literals of the name via this path, and iterate over
    shutil.move(path, destination) # this lib(shutil) can move the file into a destination we want via .move method
    print(f"moved to {path} to {destination}")
print("Receipt subtotal : $%.2f" % subtotal) # uses a special formatting
# and then remember we won't be able to get it again, because they sit inside processed, because you already calculated
# it, so we moved them to a different folder, so we won't calculate again. so we can't run it again





