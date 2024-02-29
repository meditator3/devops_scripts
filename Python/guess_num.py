print("please Guess a number between 1 and 10 :")
guess = int(input())

if guess != 5:
    print("you guessed wrong!")
    if guess < 5:
        print("please guess higher!")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("well done, you guessed on the 2nd try")
    else:
        print("well, sorry, you didn't guess it yet")
else:
    print("wow! you got it the first time !")