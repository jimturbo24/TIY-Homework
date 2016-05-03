import random

userNumber = 0
compNumber = random.randint(1, 1000)
lowBound = 1
highBound = 1000
count = 0

print('Enter a number between 1 and 1000 and the computer will try to guess it.')
while not (userNumber > 1 and userNumber < 1001):
    userNumber = int(input('Enter a number: '))
    if userNumber < 1:
        print('Enter a number greater than 1.')
    elif userNumber > 1001:
        print('Enter a number of 1000 or less.')


while count < 6:
    compNumber = random.randint(lowBound, highBound)
    if compNumber > userNumber:
        highBound = compNumber
    elif compNumber < userNumber:
        lowBound = compNumber
    else:
        print('Your number is {0}. The computer guessed it in {1} tries.'.format(compNumber, count))
        break
    count += 1

print('In 5 tries the computer guessed {0}'.format(compNumber))
