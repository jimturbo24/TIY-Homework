class Student:
    def __init__(self, firstName=None, lastName=None, GPA=None):
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA

    def isComplete(self):
        return bool(self.firstName and
                    self.lastName and
                    self.GPA is not None)

students = [Student(), Student('jim', 'turbo', 0.0), Student('bob', 'handy', 3.0)]
for item in students:
    print(item.firstName)
    print(item.lastName)
    print(item.GPA)
    print(item.isComplete())
    print("")
