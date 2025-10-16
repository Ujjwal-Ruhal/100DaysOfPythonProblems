# Here’s my code.
print('Enter a valid operator ( y, Y, n, N )')
passport = input('Passport : ')
criminal_record = input('Criminal Record : ')
visa = input('Visa : ')
visa_free = input('Visa Free : ')

li = [passport.lower() , criminal_record.lower(), visa.lower(), visa_free.lower() ]
if passport.isalpha() and criminal_record.isalpha() and visa.isalpha() and visa_free.isalpha():
    if (li[0]=='y' or li[0]=='n') and (li[1]=='y' or li[1]=='n') and (li[2]=='y' or li[2]=='n') and (li[3]=='y' or li[3]=='n'):
        if criminal_record=='y' and passport=='n':
            print('Travel denied')
        elif criminal_record=='n' and passport=='y' and (visa=='y' or visa_free=='y'):
            print('Allowed to travel')
        else:
            print('Travel denied')
    else:
        print('Invalid Input Enter a valid operator ( y, Y, n, N )')
else:
    print('Invalid Input only alphabetic characters')

'''
NOTES: Uses

if (passport in ['y', 'n']) and (criminal_record in ['y', 'n']) and (visa=='y' or visa_free=='y]):
    ...

''
if (x == 'y' or x == 'n'):
it’s a red flag — replace it with:
if x in ('y', 'n'):
''

.strip().lower() → trims spaces and handles case.
.issubset(valid) → elegant one-line validation.

''*************************************************************''
print('Enter only y/n (case-insensitive)')

passport = input('Passport: ').lower()
criminal_record = input('Criminal Record: ').lower()
visa = input('Visa: ').lower()
visa_free = input('Visa Free: ').lower()

# Validate inputs
*************************************************************************************
if not all(x in ['y', 'n'] for x in [passport, criminal_record, visa, visa_free]):
    print('Invalid input! Enter only y or n.')
*************************************************************************************    
else:
    if criminal_record == 'y' and passport == 'n':
        print('Travel denied')
    elif criminal_record == 'n' and passport == 'y' and (visa == 'y' or visa_free == 'y'):
        print('Allowed to travel')
    else:
        print('Travel denied')

''*************************************************************''

'''

#  Ai ganerated
print('Enter a valid operator (y / n)')

passport = input('Passport: ').strip().lower()
criminal = input('Criminal Record: ').strip().lower()
visa = input('Visa: ').strip().lower()
visa_free = input('Visa Free: ').strip().lower()

valid = {'y', 'n'}

if {passport, criminal, visa, visa_free}.issubset(valid):
    if passport == 'y' and criminal == 'n' and (visa == 'y' or visa_free == 'y'):
        print('Allowed to travel')
    else:
        print('Travel denied')
else:
    print('Invalid input! Please enter only y or n.')
