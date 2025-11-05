def square(n):
    return n * n  # clean, precise, reusable

try:
    num = int(input("Enter a number: "))
    result = square(num)
    print(f"Number {num} square is: {result}")

except ValueError:
    print("Invalid Input")
