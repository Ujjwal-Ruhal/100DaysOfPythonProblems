def bubble_sort(numbers):
    
    for i in range(len(numbers) - 1):
        swapped = False

        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j] , numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers

try:
    user_input = input("Enter a number separated by comma : ")
    numbers = [int(num.strip()) for num in user_input.split(",")]

    sort_numbers = bubble_sort(numbers)

    print(f"Bubble sort : {sort_numbers}")

except ValueError:
    print("Invalid Input")