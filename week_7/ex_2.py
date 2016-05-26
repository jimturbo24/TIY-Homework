def draw_histogram(aList):
    for i in aList:
        print('|', end='')
        print('#' * i)

draw_histogram([3,8,0,2])


def draw_label_histogram(aDict):
    length = 0
    for k in aDict:
        if len(k) > length:
            length = len(k)

    for i in aDict:
        print(' ' * (length-len(i)), end='')
        print(i, end=' ')
        print('|', end='')
        print('#' * aDict[i])

draw_label_histogram({'apples': 3, 'grapes': 12, 'pears': 2, 'bananas': 4})
