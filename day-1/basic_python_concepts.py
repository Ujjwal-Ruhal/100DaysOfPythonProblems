# Basic print statement
print(1)   # Output: 1

# Addition
print(1+4)   # Output: 5

# Subtraction
print(3-2)   # Output: 1
print(2-7)   # Output: -5

# Multiplication
print(2*2)     # Output: 4
print(2*2*2)   # Output: 8

# Exponentiation (2 raised to the power 3)
print(2**3)   # Output: 8

# Division (always returns float)
print(9/3)    # Output: 3.0
print(10/3)   # Output: 3.3333333333333335

# Floor division (quotient without decimal part)
print(10//3)  # Output: 3
print(11//2)  # Output: 5

# Modulus (remainder)
print(10%3)   # Output: 1

# Combination of multiplication and addition
print(2*60+30)   # Output: 150

# Brackets change the order of operations
print((30+2)*5)   # Output: 160

# Square root using power (1/2)
print(49**(1/2))   # Output: 7.0

# Slightly tricky expression:
# (8//7) = 1 → 1**(1/4) = 1 → 87 % 1 = 0
print(87%(8//7)**(1/4))   # Output: 0.0

# Float multiplication
print(2.0*3)   # Output: 6.0

# Division and subtraction together
print(9/1 - 1)   # Output: 8.0

# Division by zero (this would raise an error, so kept as a comment)
# print(9/0)   # ZeroDivisionError: division by zero

# Escape characters:
# \n = new line
print('Hey there! \nThank you')  
# Output:
# Hey there! 
# Thank you

# \t = tab space
print('Congrats \t Rs.30')  
# Output: Congrats     Rs.30

# Table-style formatting using \t and \n
print('item \t qty\nApple \t 5\nBanana \t 12')  
# Output:
# item    qty
# Apple   5
# Banana  12
