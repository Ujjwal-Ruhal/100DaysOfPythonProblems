def max_min_number(numbers):
    max_num = min_num = numbers[0]  # initialize both to first value
    
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    
    return max_num, min_num


try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    max_number, min_number = max_min_number(numbers)

    print(f"\nMaximum: {max_number}")
    print(f"Minimum: {min_number}")

except ValueError:
    print("Invalid Input")
