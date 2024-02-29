message = input("what is that message you want to echo?\n")
echo = input("and how many times you want it?\n")


def print_message(message, echo):
    if not echo :
        echo = "1"
    print("echo=", int(echo))
    for times in range(0, int(echo)):
        print(message)
    return


print_message(message, echo)
