import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False 
    return True 


def count_prime_composite(n):
    n = abs(n)
    prime_count, composite_count = 0, 0
    prime_digits, composite_digits = [], []

    while n > 0:
        digit = n % 10
        
        if digit > 1:  # ignore 0 and 1
            if is_prime(digit):
                prime_count += 1
                prime_digits.append(digit)
            else:
                composite_count += 1
                composite_digits.append(digit)
        
        n //= 10  # ← VERY IMPORTANT: inside loop

    return prime_count, composite_count, prime_digits, composite_digits


try:
    num = int(input("Enter a number: "))
    prime_count, composite_count, prime_digits, composite_digits = count_prime_composite(num)
    
    print(f"Prime Digits: {prime_digits} → Count = {prime_count}")
    print(f"Composite Digits: {composite_digits} → Count = {composite_count}")

except ValueError:
    print("Invalid Input")
