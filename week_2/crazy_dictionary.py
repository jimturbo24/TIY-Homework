with open("/usr/share/dict/words", "r") as f:
    words = f.readlines()
for word in sorted(words, reverse=True):
    print(word.strip())



#     f = open("/usr/share/dict/words", "r")
#     words = f.readlines()
#     f.close
#     rev_sort = sorted(words, reverse=True)
#     print(rev_sort[0:5])
#
# def hard_mode():
#     f = open("/usr/share/dict/words", "r")
#     words = f.readlines()
#     f.close
#     single_list = []
#     for word in words:
#         if len(word) > 1:
#             single_list.append(word)
#
#
# easy_mode()
