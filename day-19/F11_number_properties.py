import math

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


def is_prime(number):
    if number <= 1:
        return "Not Prime"
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"


def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev * sign


def is_palindrome(n):
    return "Palindrome" if n == reverse_number(n) else "Not Palindrome"


def is_armstrong(n):
    num = abs(n)
    
    # Step 1: Extract digits
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    
    # Step 2: Number of digits
    power = len(digits)

    # Step 3: Compute Armstrong total
    total = sum(d ** power for d in digits)

    return "Armstrong" if total == abs(n) else "Not Armstrong"


try:
    num = int(input("Enter a number: "))

    print(f"Even / Odd         : {even_odd(num)}")
    print(f"Prime / Not        : {is_prime(num)}")
    print(f"Palindrome / Not   : {is_palindrome(num)}")
    print(f"Armstrong / Not    : {is_armstrong(num)}")

except ValueError:
    print("Invalid Input")
