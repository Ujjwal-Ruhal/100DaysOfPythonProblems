# -------------------------------
# main.py
# Demonstration of Python Modules
# -------------------------------

# Import your own custom module (mymodule.py must be in the same folder)
import mymodule

# ***** Using Custom Module *****
print("***** Using Custom Module *****")
mymodule.greet("Ujjwal")                  # Call function from custom module
print("Addition:", mymodule.add(10, 5))   # Add numbers using module function
print("Subtraction:", mymodule.sub(15, 6))# Subtract numbers
print("Multiplication:", mymodule.mul(7, 3)) # Multiply numbers


# ***** Importing Specific Functions *****
print("\n***** Importing Specific Functions *****")
from mymodule import add, mul  # Import specific functions from custom module
print("add(5,5):", add(5, 5))
print("mul(4,6):", mul(4, 6))


# ***** Using Alias *****
print("\n***** Using Alias *****")
import mymodule as mm          # Give module a short name (alias)
print("Alias (mm.add):", mm.add(100, 50))


# ***** Using Built-in Module (math) *****
print("\n***** Using Built-in Module (math) *****")
import math                    # Import built-in math module
print("Square root of 16:", math.sqrt(16))  # sqrt() gives square root
print("Value of π:", math.pi)                # pi constant
print("2 power 5:", math.pow(2, 5))          # pow() = 2^5


# ***** Using Built-in Module (datetime) *****
print("\n***** Using Built-in Module (datetime) *****")
import datetime
print("Current date and time:", datetime.datetime.now())  # Show current date/time


# ***** Using Built-in Module (random) *****
print("\n***** Using Built-in Module (random) *****")
import random
print("Random number (1-10):", random.randint(1, 10))     # Random int between 1–10


# ***** Using Custom Functions from Another File *****
print("\n***** Using Custom Functions from Another File *****")
# Example showing reuse from custom module
num1 = 8
num2 = 12
result = mymodule.add(num1, num2)
print(f"Sum of {num1} and {num2} is:", result)


print("\nAll module demonstrations completed successfully.")
