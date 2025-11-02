try:
    star = int(input("Enter a number: "))

    if star > 0:
        for i in range(star + 1):
            print("*" * i)
    elif star == 0:
        print("Nothing print because your input is Zero")
    else:
        print("Negative values are not allow")
except ValueError:
    print("Invalid Input")
