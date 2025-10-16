# check_voting_eligibility.py

age = int(input('Enter your age: '))

if age <= 0 or age > 120:
    print('Invalid age')
elif age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
