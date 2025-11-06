def digit_analysis(n):
    n = abs(n)   
    total_sum, total_product, digit_count = 0 , 1 , 0
    
    while n > 0:
        digit = n % 10
        total_sum += digit
        total_product *= digit
        digit_count += 1
        n //= 10

    return total_sum, total_product, digit_count

try:
    num = int(input("Enter a number: "))
    total_sum, total_product, digit_count = digit_analysis(num)
    print(f"Sum = {total_sum}")
    print(f"Product = {total_product}")
    print(f"Count = {digit_count}")

except ValueError:
    print("Invalid Input")
