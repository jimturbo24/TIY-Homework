# import time
# import sys
#
# # print("something{0}{1}{2}{3}".format(".", ".", ".", "."))
# # time.sleep(4)
# # print("something else.......")
#
# sixDots = "......"
#
# def slow_dots(dots):
#     for char in dots:
#         print(char, end='')
#         sys.stdout.flush()
#         time.sleep(0.5)
#
# slow_dots(sixDots)

nums_1 = [1,2,3,4,5]
nums_2 = [1,2,3,4,5]
nums_3 = [1,2,3,4,5]
nums_4 = [1,2,3,4,5]

fourNums = nums_1+nums_2 +nums_3 +nums_4

print(nums_1)
print(fourNums)

nums_1.append(6)
fourNums.append('dog')

print(nums_1)
print(fourNums)
