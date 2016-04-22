def correctLetterAppend(aList, aChar, aWord):
    letterCount = 0
    for letter in aWord:
        if letter == aChar.lower():
            aList[letterCount] = letter
        letterCount +=1
    return aList

word = "puppies"
trys = 8

guessList= (["_"] * len(word))

print(guessList)

while trys:
    userGuess = input("You have {0} trys left. Enter a letter: ".format(trys))
    while len(userGuess) > 1 or userGuess.isdigit():
        userGuess = input("Sorry, no numbers or words please! Enter a letter: ")
    correctLetterAppend(guessList, userGuess, word)
    if userGuess not in word:
        trys -= 1
    print(guessList)



for char in guessList:
    print(char, end=" ")
print("")
