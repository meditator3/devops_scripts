my_number = 7
your_number = int(input("what's your guess? choose a number between 1-10: "))
while your_number != my_number:
    if your_number > my_number :
        your_number = int(input("guess lower (1-10): "))
    else:
        if your_number < my_number :
            your_number = int(input("guess higher(1-10): "))


print("you guessed right! its {0}".format(your_number))