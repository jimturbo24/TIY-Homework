import random

def correctLetterAppend(aList, aChar, aWord):
    letterCount = 0
    for letter in aWord:
        if letter == aChar.lower():
            aList[letterCount] = letter
        letterCount +=1
    return aList

f = open("/usr/share/dict/words", "r")
words = f.readlines()
f.close

print("""         ------ Welcome to Guess That Word! ------
To play, select which letters you think are in the mystery word.
If the letters are in the word, the computer (aka. Vanna) will reveal
where they are in the word. You can guess up to 8 letters per game. You
will only loose a guess if a letter is not in the word. Have fun!\n""")

trys = 8
word = words[random.randint(0, len(words))].strip()
displayList = (["_"] * len(word))
guessList = []

print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)))
print(word)
print(displayList)

while trys:
    userGuess = input("You have {0} trys left. Enter a letter: ".format(trys))
    while userGuess in guessList:
        userGuess = input("You guessed that letter already! Enter a new letter: ")
    while len(userGuess) > 1 or userGuess.isdigit():
        userGuess = input("Sorry, no numbers or words please! Enter a letter: ")
    correctLetterAppend(displayList, userGuess, word)
    if userGuess not in word:
        trys -= 1
    print(displayList)
    print(guessList)
    guessList.append(userGuess)

for char in guessList:
    print(char, end=" ")
print("")
