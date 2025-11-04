'''
Enter number of rows: 5

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

'''

try:
    # take input from user
    rows = int(input("Enter number of rows: "))

    # validate input
    if rows > 0:

        print()  # blank line for cleaner output spacing

        # upper half 
        for i in range(1, rows + 1):
            print(" " * ( rows - i ) , end="")
            for j in range(1,i+1):
                print(j ,end=" ")
            print()

        # lower half 
        for i in range( rows-1, 0 , -1):
            print(" " * ( rows - i ) , end="")
            for j in range(1,i+1):
                print(j ,end=" ")
            print()
        print()

    elif rows == 0:
        print("Zeros are not allowed.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input. Please enter a valid number.")