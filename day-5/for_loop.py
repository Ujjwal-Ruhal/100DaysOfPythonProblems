# -------------------------------
# FOR LOOP EXAMPLES
# -------------------------------

# Use of for loop:
# If you want to repeat a task multiple times (like printing something 100 times),
# instead of copy-pasting, you use a loop.
# A for loop executes code for each item in a sequence or for a range of numbers.

# Example 1: Loop through a list of mixed data
l = ['apple', 2, 1021, 'A', 10.23]

# Print the entire list
print(l)

# Print all values in the list using a for loop
for i in l:
    print(i)
    '''
    Output:
    apple
    2
    1021
    A
    10.23
    '''

# Example 2: Loop through another list
for x in ['hello', 'ji', 'kiya', 'haal', 'hai', 'aapke']:
    print(x)

# Example 3: Print a table of even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# Example 4: Print a multiplication table for a user input number
n = int(input('Enter a number: '))
for i in range(1, 11):  # loop from 1 to 10
    num = i * n
    print(num, '\n')

print('\n')

# Example 5: Print a message multiple times
for i in range(50):  # loop runs 50 times
    print('I Love You')

# Get the number for which the table will be printed
n = int(input("Enter a number to print its multiplication table: "))

# Get how many multiples you want
limit = 10

# Loop from 1 to limit
for i in range(1, limit + 1):
    result = n * i
    print(f"{n} x {i} = {result}")
