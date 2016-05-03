def no_double(aList):
    newList = []
    for item in aList:
        if item not in newList:
            newList.append(item)
    return newList

numList = [2,2,4,5,6,6,6,9,10,10,10,10,11]
print(no_double(numList))
