def cube(n):
    return n ** 3 

try:
    num = int(input("Enter a number: "))
    result = cube(num)
    print(f"Number {num} cube is: {result}")

except ValueError:
    print("Invalid Input")
