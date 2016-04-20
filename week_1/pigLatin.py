def pigLatin(word):
    if word[0] in "aeiou":
        wordTrunc = word[1:]
        return wordTrunc + "say"
    else:
        firstLetter = word[0]
        wordTrunc = word[1:]
        return wordTrunc + firstLetter + "ay"

def pigTranslate(sentance):
    for word in sentance.split():
        if "," in word:
            noPunc = word[0:(len(word)-1)]
            print(pigLatin(noPunc) + ",", end=" ")
        elif "." in word:
            noPunc = word[0:(len(word)-1)]
            print(pigLatin(noPunc) + ".", end=" ")
        else:
            print(pigLatin(word), end=" ")
    print("")


choice = "y"

print("This program translates words/sentances into pig latin.")

while "y" in choice.lower():
    word = input("Please enter a word/sentance: ")
    pigTranslate(word)
    choice = input("Would you like to enter another word or sentance (y/n)? ")

print("yebay-yebay!")
