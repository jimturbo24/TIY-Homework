
def correctLetterAppend(aList, aChar, aWord):
    letterCount = 0
    for letter in aWord:
        if letter.lower() == aChar.lower() or letter == "'":
            aList[letterCount] = letter
        letterCount +=1
    return aList

def randomWord():
    import random
    f = open("/usr/share/dict/words", "r")
    words = f.readlines()
    f.close
    return words[random.randint(0, len(words))].strip()

def lengthSelector(num):
    word = randomWord()
    if num == 1:
        while len(word) >= 6:
            word = randomWord()
        return word
    elif num == 2:
        while len(word) <= 6 or len(word) >= 10:
            word =randomWord()
        return word
    elif num == 3:
        while len(word) <= 10:
            word = randomWord()
        return word

playAgain = "y"

print("""         ------ Welcome to Guess That Word! ------
To play, select which letters you think are in the mystery word.
If the letters are in the word, the computer (aka. Vanna) will reveal
where they are in the word. You can guess up to 8 letters per game. You
will only loose a guess if a letter is not in the word. Have fun!\n""")

while "y" in playAgain.lower():

    diffLevel = ""

    print("Select a difficulty level:\n(1) Easy\n(2) Normal\n(3) Hard")
    while diffLevel not in ("1","2","3"):
        diffLevel = input("> ")

    trys = 8
    word = lengthSelector(int(diffLevel))
    displayList = (["_"] * len(word))
    guessList = []

    #print(word)
    if "'" in word:
        print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)-1))
    else:
        print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)))

    while trys:
        userGuess = input("You have {0} trys left. Enter a letter: ".format(trys))
        if userGuess in guessList:
            print("You guessed that letter already!")
            continue
        if len(userGuess) > 1 or userGuess.isdigit():
            print("Sorry, no numbers or words please!")
            continue
        correctLetterAppend(displayList, userGuess, word)
        if userGuess not in word:
            print("The letter {0} is not in the mystery word.".format(userGuess))
            trys -= 1
        if "_" not in displayList:
            print("\n{0} is the word. You won!".format(word))
            break
        if trys == 0:
            print("\nYou're all out of guesses. Your word was {0}".format(word))
            break
        for char in displayList:
            print(char, end=" ")
        print("")
        guessList.append(userGuess)

    playAgain = input("Wanna play again (y/n)?")
