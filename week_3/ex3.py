def is_in_list(aList, aNum):
    if aNum in aList:
        return True
    else:
        return False

print(is_in_list([1, 3, 5, 7, 9], 2))
print(is_in_list([1, 3, 5, 7, 9], 3))

def merge_lists(listA, listB):
    newList = []
    for item in listA:
        if item in listB and item not in newList:
            newList.append(item)
    return newList

a = [1, 1, 2, 3, 4, 8, 13, 21, 35, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(merge_lists(a, b))
