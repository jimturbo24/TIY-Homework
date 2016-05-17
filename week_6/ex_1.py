def get_factors(num):
    modList = []
    pairList = []
    for i in range(1, num + 1):
        if num % i == 0:
            modList.append(i)
    while modList:
        if len(modList) == 1:
            tup = (modList[0], modList.pop())
        else:
            tup = (modList.pop(0), modList.pop())
        pairList.append(tup)

    return pairList


print(get_factors(12))
print(get_factors(16))
