# def randomWord():
#     import random
#     f = open("/usr/share/dict/words", "r")
#     words = f.readlines()
#     f.close
#     return words[random.randint(0, len(words))].strip()
#
# def lengthSelector(num=1):
#     word = randomWord()
#     if num == 1:
#         while len(word) >= 6:
#             word = randomWord()
#         return word
#     elif num == 2:
#         while len(word) <= 6 or len(word) >= 10:
#             word =randomWord()
#         return word
#     elif num == 3:
#         while len(word) <= 10:
#             word = randomWord()
#         return word
#
# for item in range(0,10):
#     word = lengthSelector(1)
#     print(word, len(word))

# diffLevel = ""
#
# while diffLevel not in ("1","2","3"):
#     print(diffLevel)
#     diffLevel = input("> ")
#     print(diffLevel)

word = "jimmyies"

if "'" in word:
    print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)-1))
else:
    print("Your mystery word has {0} letters in it. Good Luck!".format(len(word)))
