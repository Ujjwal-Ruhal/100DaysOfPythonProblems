def separate_even_odd(numbers):
    even_list = []
    odd_list = []
    
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    
    return even_list, odd_list


try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    even_numbers, odd_numbers = separate_even_odd(numbers)

    print(f"Even numbers : {even_numbers}")
    print(f"Odd numbers  : {odd_numbers}")

except ValueError:
    print("Invalid Input")
