def remove_duplicated_element(F_tup , S_tup):
    unique = []
    for i in F_tup:
        if i not in unique:
            unique.append(i)
    for i in S_tup:
        if i not in unique:
            unique.append(i)
    
    return tuple(unique)

try:
    user_input = input("Enter first tuple numbers separated by comma: ")
    first_tup = tuple(int(x.strip()) for x in user_input.split(","))
    user_input = input("Enter second tuple numbers separated by comma: ")
    second_tup = tuple(int(x.strip()) for x in user_input.split(","))

    result = remove_duplicated_element(first_tup , second_tup)

    print(f"First tuple: {first_tup}")
    print(f"Second tuple: {second_tup}")
    print(f"Remove Duplicated element : {result}")

except ValueError:
    print("Invalid input, please try again")