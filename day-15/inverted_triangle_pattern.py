try:
    star = int(input("Enter number of rows: "))

    if star > 0:
        for i in range(star,0,-1):
            print("*" * i)
    elif star == 0:
        print("Nothing to print because your input is zero.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input")
