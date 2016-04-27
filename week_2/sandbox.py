# class Student:
#     def __init__(self, firstName=None, lastName=None, GPA=None):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.GPA = GPA
#
#     def isComplete(self):
#         return bool(self.firstName and
#                     self.lastName and
#                     self.GPA is not None)
#
# students = [Student(), Student('jim', 'turbo', 0.0), Student('bob', 'handy', 3.0)]
# for item in students:
#     print(item.firstName)
#     print(item.lastName)
#     print(item.GPA)
#     print(item.isComplete())
#     print("")

valuesDict = {'ace': 'ace', '2': 'two', '3': 'three',
              '4': 'four', '5': 'five', '6': 'six',
              '7': 'seven', '8': 'eight', '9': 'nine',
              '10': 'ten', 'jack': 'jack', 'queen': 'queen',
              'king': 'king'}

print(type(valuesDict))
