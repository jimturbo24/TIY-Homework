
def correctLetter_append(aList, aChar, aWord):
    """Adds a letter to a list at the same index position as a
    letter in a word, if the letters match
    """
    #letterCount = 0
    for letterCount, letter in enumerate(aWord):
        if letter.lower() == aChar.lower() or letter == "'":
            aList[letterCount] = letter
        #letterCount +=1
    return aList


def random_word():
    """Generates a word at random from a given file"""
    import random
    f = open("/usr/share/dict/words", "r")
    words = f.readlines()
    f.close
    return words[random.randint(0, len(words))].strip()


def length_selector(num=2):
    """Selects a word based upon its length"""
    word = random_word()
    if num == 1:
        while len(word) >= 6:
            word = random_word()
        return word
    elif num == 2:
        while len(word) <= 6 or len(word) >= 10:
            word =random_word()
        return word
    elif num == 3:
        while len(word) <= 10:
            word = random_word()
        return word


playAgain = "y"

print("""\n         ------ Welcome to Guess That Word! ------
To play, select which letters you think are in the mystery word.
If the letters are in the word, the computer (aka. Vanna) will reveal
where they are in the word. You can guess up to 8 letters per game. You
will only loose a guess if a letter is not in the word. Have fun!\n""")

while "y" in playAgain.lower():  # Outer game loop

    diffLevel = ""

    print("Select a difficulty level:\n(1) Easy\n(2) Normal\n(3) Hard")
    while diffLevel not in ("1","2","3"):
        diffLevel = input("> ")

    trys = 8
    word = length_selector(int(diffLevel))
    displayList = (["_"] * len(word))
    guessList = []

    if "'" in word:  # Check to remove comma from total letter count
        print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)-1))
    else:
        print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)))

    while trys:  # Inner game loop
        userGuess = input("You have {0} trys left. Enter a letter: ".format(trys))
        if userGuess in guessList:  # Check for previous letter entry
            print("You guessed that letter already!")
            continue
        if len(userGuess) > 1 or userGuess.isdigit():  # Check for word or number entry
            print("Sorry, no numbers or words please!")
            continue
        correctLetter_append(displayList, userGuess, word)
        if userGuess not in word:  # Decriment player chances if letter not in word
            print("The letter {0} is not in the mystery word.".format(userGuess))
            trys -= 1
        if "_" not in displayList:  # Winning condition
            print("\n{0} is the word. You won!".format(word))
            break
        if trys == 0:  # Loosing condition
            print("\nYou're all out of guesses. Your word was {0}".format(word))
            break
        for char in displayList:
            print(char, end=" ")
        print("")
        guessList.append(userGuess)

    playAgain = input("Wanna play again (y/n)?")
