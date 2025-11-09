def get_even(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list


def get_odd(numbers):
    odd_list = []
    for n in numbers:
        if n % 2 != 0:
            odd_list.append(n)
    return odd_list


try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]  # convert once
    
    even = get_even(numbers)
    odd = get_odd(numbers)

    print(f"Even: {even}")
    print(f"Odd : {odd}")

except ValueError:
    print("Invalid Input. Please enter only numbers separated by commas.")
