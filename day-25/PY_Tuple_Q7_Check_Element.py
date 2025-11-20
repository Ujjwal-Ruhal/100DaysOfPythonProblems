try:
    user_input = input("Enter numbers separated by comma : ")
    numbers = tuple(int(x.strip()) for x in user_input.split(","))

    find_num = int(input("Enter a number to search : "))

    if find_num in numbers:
        print("Element found")
    else:
        print("Element not found")

except ValueError:
    print("Invalid Input. Please enter numbers only.")
