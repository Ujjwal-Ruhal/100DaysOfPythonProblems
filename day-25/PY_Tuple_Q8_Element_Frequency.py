def count_frequency(tup, value):
    return tup.count(value)

try:
    user_input = input("Enter numbers separated by comma : ")
    numbers = tuple(int(x.strip()) for x in user_input.split(","))

    val = int(input("Enter element to count : "))

    result = count_frequency(numbers, val)
    print(f"the tuple is : {numbers}")
    print(f"Element {val} occurs {result} times")

except ValueError:
    print("Enter a valid number, please try again")