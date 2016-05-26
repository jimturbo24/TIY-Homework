def overlap(aList, bList):
    for i in bList:
        if i in aList:
            return True
    return False

print(overlap([1,2,3], [3,2]))
print(overlap([1,2,3], [4,5,6]))

def get_overlap(aList, bList):
        overlapList = []
        for i in bList:
            if i in aList:
                overlapList.append(i)
        return overlapList

print(get_overlap([1,2,3], [3,2]))
print(get_overlap([1,2,3], [4,5,6]))
