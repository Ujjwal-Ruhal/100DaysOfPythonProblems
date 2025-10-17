age = int(input('Enter your age: '))
experience = int(input('Enter your experience (in years): '))
qualification = input('Enter your qualification: ').strip().upper()

valid_qualifications = {'B.TECH', 'MCA'}

if not (21 <= age <= 35):
    print('Not eligible due to age')
elif experience < 2:
    print('Not eligible due to experience')
elif qualification not in valid_qualifications:
    print('Not eligible due to qualification')
else:
    print('Eligible')
