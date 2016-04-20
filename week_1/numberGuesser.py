import random

def numberGenerator(a = 1, b = 1000):
    return random.randint(a, b)

randomNum = numberGenerator()

print("Guess a number between 1 and 1000")
userGuess = int(input("Enter your guess: "))

if userGuess == randomNum:
    print("Correct")
elif userGuess > randomNum:
    print("Too high!")
else:
    print("Too low!")
