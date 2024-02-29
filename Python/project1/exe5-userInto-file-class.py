def get_file_name(reprompt=False): # promprts the reprompt as false by default!
    if reprompt: # if reprompt = true
        print("enter file name: ")
    file_name = input("Destination file name: ").strip()
    return file_name() or get_file_name(reprompt=True) # call the function get_file_name again if filename isn't true


file_name = get_file_name()

print(f"enter your content . Entering an empty line will write the content to {file_name}")
with open(file_name, "w") as f:
    eof = False #end of file
    lines = []
    while not eof:
        line = input()
        if line.strip():
            line.append(f"{line}\n")
        else:
            eof = True

    f.writelines(lines)
    print(f"lines written into {file_name}")