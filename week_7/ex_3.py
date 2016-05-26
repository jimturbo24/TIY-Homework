firstName = ''
lastName = ''
print('Please enter your first and last name, with each having two characters.')
while len(firstName) < 2
      or len(lastName) < 2
      or not firstName.isalpha()
      or not lastName.isalpha():
    firstName = input('Enter your first name: ')
    lastName = input('Enter you last name: ')
print(lastName + ', ' + firstName)
