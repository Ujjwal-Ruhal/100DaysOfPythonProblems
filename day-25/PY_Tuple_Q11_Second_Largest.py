def second_largest(tup):
    # Step 1: Ensure tuple has at least 2 unique values
    unique_list = []
    for i in tup:
        if i not in unique_list:
            unique_list.append(i)

    if len(unique_list) < 2:
        return "No second largest (values are not distinct)"
    
    # Step 2: Find largest and second largest manually
    largest = second = unique_list[0]

    for num in unique_list:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second


try:
    user_input = input("Enter numbers separated by comma: ")
    numbers = tuple(int(x.strip()) for x in user_input.split(","))

    result = second_largest(numbers)
    print(f"Tuple: {numbers}")
    print(f"Second Largest Element: {result}")

except ValueError:
    print("Invalid Input! Please enter only integers.")
