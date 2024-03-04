with open('xmen_base.txt', 'a') as f: # 'a' is appending into file
    f.write('Professor Xavier\n')

# now f represents the file xmen_base.txt

f = open('xmen_base.txt', 'a')
with f:
    f.write("Something\n")

with open('xmen_base.txt', 'r') as f:
    print(f.read())

# now every run will add something and Prof.
