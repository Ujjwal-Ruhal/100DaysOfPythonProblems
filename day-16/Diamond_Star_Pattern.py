'''
Enter number of rows: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

try:
    rows = int(input("Enter number of rows: "))

    if rows > 0:
        # Upper half
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

        # Lower half
        for i in range(rows - 1, 0, -1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

    elif rows == 0:
        print("Nothing to print because your input is zero.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input")
