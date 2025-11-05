def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"
  
try:
    num = int(input("Enter a number: "))
    result = is_even(num)
    print(f"Number {num} is : {result}")

except ValueError:
    print("Invalid Input")