'''
Program: Pascal's Triangle
--------------------------
Example Output:
Enter number of rows: 6

      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
'''

def factorial(n):
    """Return factorial of a number"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    rows = int(input("Enter number of rows: "))

    if rows > 0:
        print("\n")  # spacing before output

        for i in range(rows):
            # print leading spaces for centering
            print(" " * (rows - i), end="")
            
            # print numbers in the row
            for j in range(i + 1):
                val = factorial(i) // (factorial(j) * factorial(i - j))
                print(f"{val} ", end="")
            print()  # move to next line

    elif rows == 0:
        print("Zero rows are not allowed.")
    else:
        print("Negative values are not allowed.")

except ValueError:
    print("Invalid Input. Please enter a valid integer.")
