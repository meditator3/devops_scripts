"""
suppose we want to read from xmen_base.txt
"""

xmen_file = open("xmen_base.txt", 'r') # we want to open by read (,'r')
print(xmen_file)
print("ffffffffffffffffffff")
#if want to print it, it won't work, because its not yet configured
# we get textwrapper object
# so we need to add .read()

print(xmen_file.read())
print(xmen_file.read())
print(xmen_file.read())
print(xmen_file.read())
# if we try to reprint it - it won't work
# because the cursor that reads it, is at the END
# so we need to add .seek(0) {0, is character location}
xmen_file.seek(0)
print(xmen_file.read())
#now we need to use seek again if we want to read the file again
xmen_file.seek(0)
for line in xmen_file:
    print(line, end="")
xmen_file.close() # makes the file inaccessible
print(xmen_file.read()) # this will create an error, because we closed the file
# pay attention that we opened the file to read from it,
# if we want to write on it, we should open it accordingly

