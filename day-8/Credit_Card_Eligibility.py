age = int(input('Enter your age: '))
income = int(input('Enter your income: '))

if 18 <= age <= 120:
    print('Eligible for credit card' if income > 10000 else 'Low Income')
else:
    print('Not eligible')
