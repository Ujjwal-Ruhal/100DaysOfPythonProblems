'''
Program: Half Diamond Star Pattern
----------------------------------
Example Output:
Enter number of rows: 5

*
**
***
****
*****
****
***
**
*
'''

try:
    # take input from user
    rows = int(input("Enter number of rows: "))

    # validate input
    if rows > 0:
        print()  # blank line for cleaner output spacing

        # upper half (increasing stars)
        for i in range(1, rows + 1):
            print("*" * i)

        # lower half (decreasing stars)
        for j in range(rows - 1, 0, -1):
            print("*" * j)

    elif rows == 0:
        print("Zeros are not allowed.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input. Please enter a valid number.")
