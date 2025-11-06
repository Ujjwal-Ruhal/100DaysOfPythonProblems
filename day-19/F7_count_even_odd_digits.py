def count_even_odd(n):
    n = abs(n)
    even_count, odd_count = 0, 0
    
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    
    return even_count, odd_count


try:
    num = int(input("Enter a number: "))
    even, odd = count_even_odd(num)
    
    print(f"Even Digits: {even}")
    print(f"Odd Digits : {odd}")

except ValueError:
    print("Invalid Input")
