# write code that accepts a file name and then accepts lines and puts them into/write them
# into that file, and then without pressing anything will exit the input mode, and close file.

file_name = input('type your file name: ')

file_name_revised = file_name + ".txt"
opened_file = open(file_name_revised, "w")
print(file_name_revised)
while True:
    line = input("type your line here: ")
    if line == "":
        break
    opened_file.write(line + "\n")
