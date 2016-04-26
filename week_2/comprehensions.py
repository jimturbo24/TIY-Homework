import csv
import datetime
# Easy
# 1.
# phrase = "List Comprehensions are the Greatest!"
#
# noVowel = "".join([letter for letter in phrase if letter not in "aeiou"])
#
# print(noVowel)

# 2.
# studentGrades = {'Inara': {'Homework 1': 90, 'Homework 2': 94, 'Homework 3': 90},
#                  'Mal': {'Homework 1': 50, 'Homework 2': 100, 'Homework 3': 60},
#                  'Simon': {'Homework 1': 98, 'Homework 2': 96, 'Homework 3': 96},
#                  'River': {'Homework 1': 100, 'Homework 2': 100, 'Homework 3': 0}
#                  }
#
# def avg_grades(aStudent):
#         total = 0
#         for homeWork in studentGrades[aStudent]:
#             total += studentGrades[aStudent][homeWork]
#         return int(total / len(studentGrades[aStudent]))
#
# studentAvg = {student: avg_grades(student) for student in studentGrades}
# print(studentAvg)

# 3.
# with open("/usr/share/dict/words", "r") as f:
#     words = f.readlines()
#
# aceList = [word for word in words if word.strip().endswith("ace")]
#
# for aceWord in aceList:
#     print("{0} Ventura, pet detective!".format(aceWord.strip().capitalize()))

# 4.
# homeworkGrades = [studentGrades[student]['Homework 3'] for student in studentGrades]
# avg = sum(homeworkGrades) / len(homeworkGrades)
# print(avg)

# Normal mode
# f = open('wavedata.csv')
# waveData = csv.reader(f)
# f.close

# 1.
# waterTemps = [row[4] for row in waveData]
# print(waterTemps)

# 2.
# waterTempsFahr = [((float(row[4])*1.8) + 32) for row in waveData]
# for temp in waterTempsFahr:
#     print("{0:.1f}".format(temp))

# 3.
# dateList = [row[5].split('-') for row in waveData]
# for aDate in dateList:
#     print(datetime.date(int(aDate[0]), int(aDate[1]), int(aDate[2])))

# 4.
# wavesByDate = {row[5]: row[1] for row in waveData}
# print(wavesByDate)

# Hard mode
# 1.
