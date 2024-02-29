with open('xmen_base.txt', 'a') as f: # 'a' is appending into file
    f.write('Professor Xavier\n')

# now f represents the file xmen_base.txt

f = open('xmen_base.txt', 'a')
with f:
    f.write("Something\n")
    