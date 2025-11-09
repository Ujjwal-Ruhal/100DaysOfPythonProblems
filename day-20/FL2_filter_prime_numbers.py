import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
    return True 

def get_primes(numbers):
    prime_list = []
    for i in numbers:
        if is_prime(i):
            prime_list.append(i)
    return prime_list

try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]
    
    primes = get_primes(numbers)
    print(f"Prime numbers: {primes}")

except ValueError:
    print("Invalid Input. Enter numbers only.")
