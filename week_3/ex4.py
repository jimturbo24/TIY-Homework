def max_of_three_list(aList):
    maxItem = 0
    for i in aList:
        for  x in aList:
            if i > x:
                maxItem = i
    return maxItem

def max_of_three(*num):
    maxItem = num[0]
    for i in num:
        if i > maxItem:
            maxItem = i
    return maxItem

print(max_of_three_list([4, 7, 3]))
print(max_of_three(4, 7, 3))
