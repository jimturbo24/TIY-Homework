choice = "defalty"

print("This program translates words into pig latin.")

while "y" in choice.lower():
    word = input("Please enter a word: ")

    if word[0] in "aeiou":
        wordTrunc = word[1:]
        print(word + " in pig latin is " + wordTrunc + "say")
    else:
        firstLetter = word[0]
        wordTrunc = word[1:]
        print(word + " in pig latin is " + wordTrunc + firstLetter + "ay")

    choice = input("Would you like to enter another word (y/n)? ")
    if "y" in choice.lower():
        continue

print("yebay-yebay!")
