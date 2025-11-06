import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False 
    return True 


def sum_prime_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        
        if digit > 1 and is_prime(digit):  # ignore 0 and 1
            total += digit
        
        n //= 10  # ← VERY IMPORTANT: inside loop

    return total 


try:
    num = int(input("Enter a number: "))
    total = sum_prime_digits(num)
    print(f"Sum of prime digits : {total}")

except ValueError:
    print("Invalid Input")
