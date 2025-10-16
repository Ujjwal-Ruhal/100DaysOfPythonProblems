x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

if x >= y and x >= z:
    print(f'{x, y, z} -> The greatest value is: {x}')
elif y >= x and y >= z:
    print(f'{x, y, z} -> The greatest value is: {y}')
else:
    print(f'{x, y, z} -> The greatest value is: {z}')
