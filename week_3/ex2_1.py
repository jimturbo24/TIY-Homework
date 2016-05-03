def first_and_last(aList):
    newList = []
    newList.append(aList[0])
    newList.append(aList[len(aList)-1])
    return newList

numList = [5, 10, 15, 20, 25]
print(first_and_last(numList))
