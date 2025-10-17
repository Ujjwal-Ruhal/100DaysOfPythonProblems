try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    third_num = int(input("Enter third number: "))

    if first_num == second_num == third_num:
        result = "All numbers are equal"
    else:
        result = max(first_num, second_num, third_num)

    print(f"The greatest number among {first_num}, {second_num}, {third_num} is: {result}")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
