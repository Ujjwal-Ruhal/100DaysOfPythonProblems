# -------------------------------
# main.py
# Demonstration of Python Modules
# -------------------------------

# Import your own custom module
import mymodule

# Using functions from the custom module
print("***** Using Custom Module *****")
mymodule.greet("Ujjwal")
print("Addition:", mymodule.add(10, 5))
print("Subtraction:", mymodule.sub(15, 6))
print("Multiplication:", mymodule.mul(7, 3))


print("\n***** Importing Specific Functions *****")
from mymodule import add, mul
print("add(5,5):", add(5, 5))
print("mul(4,6):", mul(4, 6))


print("\n***** Using Alias *****")
import mymodule as mm
print("Alias (mm.add):", mm.add(100, 50))


print("\n***** Using Built-in Module (math) *****")
import math
print("Square root of 16:", math.sqrt(16))
print("Value of π:", math.pi)
print("2 power 5:", math.pow(2, 5))


print("\n***** Using Built-in Module (datetime) *****")
import datetime
print("Current date and time:", datetime.datetime.now())


print("\n***** Using Built-in Module (random) *****")
import random
print("Random number (1-10):", random.randint(1, 10))


print("\n***** Using Custom Functions from Another File *****")
# Example showing reuse from custom module
num1 = 8
num2 = 12
result = mymodule.add(num1, num2)
print(f"Sum of {num1} and {num2} is:", result)

print("\nAll module demonstrations completed successfully.")
