def reverse_number(n):
    sign = -1 if n < 0 else 1   # preserve negative sign
    n = abs(n)
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    
    return rev * sign

try:
    num = int(input("Enter a number: "))
    result = reverse_number(num)
    print(f"Reversed Number: {result}")

except ValueError:
    print("Invalid Input")
