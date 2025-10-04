# =====================================
# Python 'if' Statement Examples
# =====================================

# 1️⃣ Basic if example
num = 10
if num > 5:
    print(" The number is greater than 5")

# Output: The number is greater than 5


# 2️⃣ if with equality check
x = 7
if x == 7:
    print(" x is exactly 7")

# Output: x is exactly 7


# 3️⃣ if with not equal (!=)
age = 18
if age != 15:
    print(" Age is not equal to 15")

# Output: Age is not equal to 15


# 4️⃣ if with user input
user_num = int(input("Enter a number: "))
if user_num % 2 == 0:
    print(" The number is even")

# Example input: 8 → Output: The number is even


# 5️⃣ if with string comparison
name = "Alice"
if name == "Alice":
    print(" Hello, Alice! Welcome back.")

# Output: Hello, Alice! Welcome back.


# 6️⃣ if with multiple conditions using AND
marks = 85
if marks > 80 and marks <= 100:
    print(" Excellent! You scored above 80.")

# Output: Excellent! You scored above 80.


# 7️⃣ if with OR operator
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print(" It's weekend!")

# Output: It's weekend!


# 8️⃣ Nested if statements
num = 25
if num > 10:
    print(" Number is greater than 10")
    if num > 20:
        print("   Number is also greater than 20")

# Output:
# Number is greater than 10
# Number is also greater than 20


# 9️⃣ if with boolean variable
is_raining = True
if is_raining:
    print(" Don’t forget your umbrella!")

# Output: Don’t forget your umbrella!


# 🔟 if checking membership in a list
fruits = ["apple", "banana", "mango"]
if "banana" in fruits:
    print(" Banana is in the list!")

# Output: Banana is in the list!
