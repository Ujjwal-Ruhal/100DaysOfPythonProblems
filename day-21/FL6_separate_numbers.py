def separate_number(numbers):
    positive , negative , zero = [],[],[]
    for i in numbers:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)
    
    return positive, negative, zero

try:
    user_input = input("Enter a number sepated by comma :")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    positive, negative, zero = separate_number(numbers)

    print(f"\nPositive : {positive}")
    print(f"Negative : {negative}")
    print(f"Zero     : {zero}")



except ValueError:
    print("Invalid Input")