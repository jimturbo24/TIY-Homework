import random

def numberGenerator(a = 1, b = 1000):
    return random.randint(a, b)

randomNum = numberGenerator()
count = 1

print("Guess a number between 1 and 1000. You have 5 chances!")

while count < 6:
    userGuess = input("Enter guess #" + str(count) + ": ")

    if userGuess.isdigit():
        if int(userGuess) == randomNum:
            print("Correct")
        elif int(userGuess) > randomNum:
            print("Too high!")
        else:
            print("Too low!")

        count += 1
    else:
        print("I don't think you entered a number. Try again.")

print("Thanks for playing.")
