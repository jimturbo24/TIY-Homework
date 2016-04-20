import random

def numberGenerator(a = 1, b = 1000):
    return random.randint(a, b)

randomNum = numberGenerator()

print("Guess a number between 1 and 1000")
userGuess = input("Enter your guess: ")

if userGuess == randomNum:
    print("Correct")
else:
    print("Incorrect")
