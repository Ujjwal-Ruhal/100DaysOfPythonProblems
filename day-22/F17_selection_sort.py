def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


try:
    user_input = input("Enter numbers seprated by comma : ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    sorted_value = selection_sort(numbers)
    print(f"Selection Sort : {sorted_value}")

except ValueError:
    print("Invalid Input")