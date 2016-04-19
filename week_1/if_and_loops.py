nameList = []
colorList = []
ageList = []

choice = "defaulty"

while "y" in choice or "Y" in choice:
    name = input("Enter a name: ")
    nameList.append(name)
    color = input("Enter a favorite color: ")
    colorList.append(color)
    age = input("Enter an age: ")
    ageList.append(age)

    choice = input("Would you like to enter another name, color, and age (y/n)?")
    if "y" in choice or "Y" in choice:
        continue

while nameList:
    print("Name:" + nameList.pop() + " Color:" + colorList.pop() + " Age:" + ageList.pop(), end=' --- ')

print("")
