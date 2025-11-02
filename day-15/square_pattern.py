try:
    num = int(input("Enter number of rows: "))

    if num > 0:
        for i in range(num):
            print("* " * num)
    elif num == 0:
        print("Nothing to print because your input is zero.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input")
