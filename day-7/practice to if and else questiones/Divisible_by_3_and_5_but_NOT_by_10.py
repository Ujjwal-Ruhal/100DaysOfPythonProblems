num = int(input('Enter a number: '))

if num % 3 == 0 and num % 5 == 0 and num % 10 != 0:
    print('Yes')
else:
    print('No')
