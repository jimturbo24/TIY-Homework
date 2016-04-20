import random

def numberGenerator(a = 1, b = 1000):
    return random.randint(a, b)

randomNum = numberGenerator()
count = 5

print("Guess a number between 1 and 1000. You have 5 chances!")

while count:
    userGuess = int(input("Enter guess #" + str(count) + ": "))

    if userGuess == randomNum:
        print("Correct")
    elif userGuess > randomNum:
        print("Too high!")
    else:
        print("Too low!")

    count -= 1

print("Thanks for playing.")
