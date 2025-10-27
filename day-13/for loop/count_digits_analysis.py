try:
    num = int(input("Enter a number: "))

    if num >= 0:
        digits = str(num)
        total_digits = len(digits)
        even, odd, total_sum = 0, 0, 0

        for d in digits:
            d = int(d)
            total_sum += d
            if d % 2 == 0:
                even += 1
            else:
                odd += 1

        print(f"Total Digits : {total_digits}")
        print(f"Even Digits  : {even}")
        print(f"Odd Digits   : {odd}")
        print(f"Sum of Digits: {total_sum}")
    else:
        print("Invalid input: Only positive numbers are allowed.")
except ValueError:
    print("Invalid input: Please enter a valid integer.")
