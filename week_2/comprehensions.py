# phrase = "List Comprehensions are the Greatest!"
#
# noVowel = "".join([letter for letter in phrase if letter not in "aeiou"])
#
# print(noVowel)

studentGrades = {'Inara': {'Homework 1': 90, 'Homework 2': 94, 'Homework 3': 90},
                 'Mal': {'Homework 1': 50, 'Homework 2': 100, 'Homework 3': 60},
                 'Simon': {'Homework 1': 98, 'Homework 2': 96, 'Homework 3': 96},
                 'River': {'Homework 1': 100, 'Homework 2': 100, 'Homework 3': 0}
                 }
#
# def avg_grades(aStudent):
#         total = 0
#         for homeWork in studentGrades[aStudent]:
#             total += studentGrades[aStudent][homeWork]
#         return int(total / len(studentGrades[aStudent]))
#
# studentAvg = {student: avg_grades(student) for student in studentGrades}
# print(studentAvg)


# with open("/usr/share/dict/words", "r") as f:
#     words = f.readlines()
#
# aceList = [word for word in words if word.strip().endswith("ace")]
#
# for aceWord in aceList:
#     print("{0} Ventura, pet detective!".format(aceWord.strip().capitalize()))

homeworkAvg = [studentGrades[student]['Homework 3'] for student in studentGrades]
# homeworkGrades = ^^^
# avg = sum(homeworkGrades) / len(homeworkGrads)

print(homeworkAvg)
avg = 0
for grade in homeworkAvg:
    avg += grade
print(avg / len(homeworkAvg))
