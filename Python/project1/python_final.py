# read from file
# function that extracts certain elements from file

with open("log.txt", 'r') as f:
    print(f.read())
    f.seek(0)
    # get names
    full_log_list = f.readlines() # saves all log in an array, each line has an index
    f.seek(0)

print(full_log_list)
def get_one_name(line): # this gets a name from the line
    name = ""
    for index in line:
        if index != ":" :   # from start of line until it meets ":"
           name += index
        else:
            break
    return name

first_name = get_one_name(full_log_list[0]) # this is line 0 where Gil is the first



def get_all_names(log): # this function returns an array of names of all participants
                             # (Gil, Eli.....and then again Gil, Eli)first name is a marker
    group_names = [first_name]
    index_of_log = 1  # because we got the first name already

    while get_one_name(log[index_of_log]) != first_name: # until you get to the first name again, that way you get all the names
        print(get_one_name(log[index_of_log]))
        group_names.append(get_one_name(log[index_of_log]))
        index_of_log +=1
    return group_names


def get_day(line):
    current_word = ""
    for part in line:
        if (part ==" ") and current_word!=True : #whenever you meet a spacebar starts build a word
            current_word += part
        if current_word:
            current_word += part
        print(current_word)

        if current_word and part == " ":
            current_word =""


get_day(full_log_list[0])
names = get_all_names(full_log_list)
print(names)
    # when all names match certain time
    # "I can do" is availability and "My yard" at [name] place




