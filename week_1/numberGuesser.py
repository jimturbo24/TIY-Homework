import random

def numberGenerator(a = 1, b = 1000):
    return random.randint(a, b)

print(numberGenerator())
print(numberGenerator(1,10))
