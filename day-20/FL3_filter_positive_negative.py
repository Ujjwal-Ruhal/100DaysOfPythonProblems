def get_positive(numbers):
    positive_list = []
    for i in numbers:
        if i > 0:
            positive_list.append(i)

    return positive_list

def get_negative(numbers):
    negative_list = []
    for i in numbers:
        if i < 0:
            negative_list.append(i)

    return negative_list

try:
    user_input = input("Enter a number separated by comma : ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    positive = get_positive(numbers)
    negative = get_negative(numbers)

    print(f"Positive : {positive}")
    print(f"Negative : {negative}")

except ValueError:
    print("Invalid Input")