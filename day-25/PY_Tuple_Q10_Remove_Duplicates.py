def unique_element(tup):
    unique_values = []
    for i in tup:
        if i not in unique_values:
            unique_values.append(i)

    return tuple(unique_values)

try:
    user_input = input("Enter numbers separated by comma : ")
    numbers = tuple(int(x.strip()) for x in user_input.split(","))

    result = unique_element(numbers)
    print(f"Original tuple: {numbers}")
    print(f"Tuple with unique values : {result}")

except ValueError:
    print("invalid input, please try again")