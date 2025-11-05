def sum_of_digits(n):
    n = abs(n)  # handle negative numbers
    total = 0
    while n > 0:
        total += n % 10      # get last digit
        n //= 10             # remove last digit
    return total

try:
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print(f"Sum of digits of {num}: {result}")

except ValueError:
    print("Invalid Input")
