'''
Enter number of rows: 5
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

'''

try:
    rows = int(input("Enter number of rows: "))

    if rows > 0:
        for i in range(rows , 0 , -1):
            print(" " * (rows-i),end="")
            for j in range(1,i+1):
                print( j ,end=" " )
            print()
    elif rows == 0:
        print("Nothing to print because your input is zero.")
    else:
        print("Negative values are not allowed.")
except ValueError:
    print("Invalid Input")