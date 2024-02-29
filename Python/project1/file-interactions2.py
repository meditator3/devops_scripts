# this copies a file xmen_base.txt to new_xmen.txt
# we opened a file called xmen_base.txt
# then we opened a new file called new_xmen.txt with write enabled
# then we wrote into the new file, the file/variable
# which then created and copied the content of xmen_base.txt to
# new_xmen.txt



xmen_file = open('xmen_base.txt', 'r')
xmen_base = open('xmen_base.txt')
new_xmen = open('new_xmen.txt', 'w')
new_xmen.write(xmen_base.read())
new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
# .name is instead of naming it "new_xmen.txt" and accessing it via the variable
# and r+ means read and write
print(new_xmen.read())
new_xmen.seek(0)
new_xmen.write("Beast\n")
new_xmen.write("Phoenix") # this will have left overs from wolverine. "Phoenixne"
new_xmen.seek(0)
print(new_xmen.read())
# this will override the previous lines. and NOT add the write.