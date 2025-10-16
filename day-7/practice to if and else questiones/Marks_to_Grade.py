marks = int(input('Enter your marks: '))

if not 0 <= marks <= 100:
    print('Invalid Marks')
elif marks >= 90:
    print('A')
elif marks >= 75:
    print('B')
elif marks >= 50:
    print('C')
else:
    print('Fail')
