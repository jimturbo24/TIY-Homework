import random

f = open("/usr/share/dict/words", "r")
words = f.readlines()
f.close

count = 1

print("""         ------ Welcome to Guess That Word! ------
To play, selecct which letters you think are in the mystery word.
If the letters are in the word, the computer (aka. Vannah) will reveal
where they are in the word. You can guess up to 8 letters per game. You
will only loose a guess if a letter is not in the word\n""")

word = words[random.randint(0, len(words))].strip()
print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)))
print(word)

while count < 9:
    letter = input("Guess #{0}. Enter a letter: ".format(count))
    print(letter)
    count += 1



# count = 20
# while count:
#
    # count -= 1
