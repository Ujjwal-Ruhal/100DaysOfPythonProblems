# ============================================
# Python Conditional Statements Documentation
# ============================================

"""
This file explains the usage of conditional statements in Python:
    - if statement
    - elif statement
    - else statement

Conditional statements are used to make decisions in a program.
They allow the program to execute different blocks of code
based on certain conditions.
"""

# --------------------------------------------
# 1️⃣ Basic IF Statement
# --------------------------------------------

# Syntax:
# if condition:
#     # code to execute when condition is True

age = 20

if age >= 18:
    print("You are an adult.")  # This will execute because 20 >= 18

# Output: You are an adult.


# --------------------------------------------
# 2️⃣ IF–ELSE Statement
# --------------------------------------------

# Syntax:
# if condition:
#     # code if condition is True
# else:
#     # code if condition is False

number = -5

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative or zero.")

# Output: The number is negative or zero.


# --------------------------------------------
# 3️⃣ IF–ELIF–ELSE Statement
# --------------------------------------------

# Syntax:
# if condition1:
#     # code block 1
# elif condition2:
#     # code block 2
# else:
#     # code block 3

marks = 72

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# Output: Grade: B


# --------------------------------------------
# 4️⃣ Nested IF Statements
# --------------------------------------------

# You can place an if statement inside another if statement.

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")

# Output: Login successful!


# --------------------------------------------
# 5️⃣ Using Logical Operators in IF Conditions
# --------------------------------------------

# and → All conditions must be True
# or  → At least one condition must be True
# not → Reverses the condition (True becomes False, and vice versa)

temperature = 28
weather = "sunny"

if temperature > 25 and weather == "sunny":
    print("It's a good day for a picnic!")

# Output: It's a good day for a picnic!


# --------------------------------------------
# 6️⃣ Short-Hand IF and IF–ELSE
# --------------------------------------------

# When you have only one statement to execute, you can write it on one line.

x = 10
y = 20

if x < y: print("x is smaller than y")  # Short-hand if

# Short-hand if–else:
print("x is smaller") if x < y else print("x is greater or equal")

# Output:
# x is smaller than y
# x is smaller


# --------------------------------------------
# 7️⃣ Combining Conditions and Comparisons
# --------------------------------------------

# You can compare multiple values or use range checks directly.

num = 15

if 10 <= num <= 20:
    print("Number is between 10 and 20")

# Output: Number is between 10 and 20


# --------------------------------------------
#  Summary
# --------------------------------------------
"""
✅ 'if' executes a block when a condition is True.
✅ 'elif' lets you test multiple conditions.
✅ 'else' runs only if all previous conditions are False.
✅ You can nest conditions or use logical operators (and/or/not).
✅ Shorthand versions exist for simple cases.
"""

print("\n✅ End of if-else documentation example.")
