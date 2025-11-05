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


try:
    num = int(input("Enter a number: "))
    result = is_palindrome(num)
    print(result)

except ValueError:
    print("Invalid Input")
