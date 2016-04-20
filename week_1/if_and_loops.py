nameList = []
colorList = []
ageList = []

choice = "defaulty"

while "y" in choice.lower():
    name = input("Enter first and last name: ")
    if not name or len(name.split()) < 2:
        print("Invalid input, please start again")
        continue
    color = input("Enter a favorite color: ")
    if not color:
        print("Invalid input, please start again")
        continue
    age = input("Enter an age: ")
    if not age or not age.isdigit():
        print("Invalid input, please start again")
        continue
    ageList.append(age)
    nameList.append(name)
    colorList.append(color)

    choice = input("Would you like to enter another name, color, and age (y/n)?")
    if "y" in choice.lower():
        continue

while nameList:
    print("Name:" + nameList.pop() + " Color:" + colorList.pop() + " Age:" + ageList.pop(), end=' --- ')

print("")
