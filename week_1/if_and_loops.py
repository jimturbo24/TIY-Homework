nameList = []
colorList = []
ageList = []

choice = "defaulty"

while "y" in choice.lower():

    name = color = age = ""

    while not name or len(name.split()) < 2:
        name = input("Enter first and last name: ")

    while not color:
        color = input("Enter a favorite color: ")

    while not age or not age.isdigit():
        age = input("Enter an age: ")

    ageList.append(age)
    nameList.append(name)
    colorList.append(color)

    choice = input("Would you like to enter another name, color, and age (y/n)?")
    #if "y" in choice.lower():
    #    continue

while nameList:
    print("Name:" + nameList.pop() + " Color:" + colorList.pop() + " Age:" + ageList.pop(), end=' --- ')

print("")
