try:
    num = int(input("Enter a number: "))

    if num == 0:
        result = "Zero"
    else:
        sign = "Positive" if num > 0 else "Negative"
        parity = "Even" if num % 2 == 0 else "Odd"
        result = f"{sign} and {parity}"

    print(f"{num} is {result}")

except ValueError:
    print("Invalid input")
