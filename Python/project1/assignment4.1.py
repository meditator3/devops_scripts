
#the idea to create an already upped string of the original version and then compare
# between them: changes to lower if there is no change
# retain the upped version if there is change

def swapped_string(string_original):
    string_upped = string_original.upper()  # this is to compare
    string_swapped = ""             # define the output type
    for i in range(0, len(string_original)):            #running on all index of original string
        if string_original[i] != string_upped[i]:       # if there is change from the original
            string_swapped += string_upped[i]    # retain the upped version, as it should be swapped
        else:               # if there is no change then it should be lowered
            string_swapped += string_original[i].lower() # lowering the original and keeping it in the swapped
    return string_swapped               # return the value of the whole swapped string

string_original = "SoMmeThInnnGG tOO BbBbB RePlAcEd"
print()
print(f"{string_original} => {swapped_string(string_original)}")
