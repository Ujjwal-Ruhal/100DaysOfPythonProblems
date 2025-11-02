try:
    num = int(input("Enter a number: "))

    if num > 0:
        for i in range(1,11):
            print(f"{num} X {i} = {num * i}")
    elif num == 0:
        print("Multiplication table of 0 is always 0")
    else:
        print("Negative Number, Please enter a positive number")

except (ValueError):
    print("Invalid Input")