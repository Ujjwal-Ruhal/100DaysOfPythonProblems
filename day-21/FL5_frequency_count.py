def frequency_count(numbers):
    freq = {}
    for n in numbers:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq


try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    result = frequency_count(numbers)

    for num, count in result.items():
        print(f"{num} → {count} times")

except ValueError:
    print("Invalid Input")
