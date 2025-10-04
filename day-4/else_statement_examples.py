# =====================================
# Python 'else' Statement Examples
# =====================================

# 1️⃣ Basic if–else example
num = 8
if num > 10:
    print(" The number is greater than 10")
else:
    print(" The number is less than or equal to 10")

# Output: The number is less than or equal to 10


# 2️⃣ Check even or odd number
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(" The number is even")
else:
    print(" The number is odd")

# Example input: 7 → Output: The number is odd


# 3️⃣ Using if–else with strings
name = input("Enter your name: ")
if name == "Alice":
    print(" Welcome, Alice!")
else:
    print(" Hello, stranger!")

# Example: input "Bob" → Output: Hello, stranger!


# 4️⃣ if–else with logical operators
age = 17
if age >= 18 and age <= 60:
    print(" You are eligible to work.")
else:
    print(" You are not eligible to work.")

# Output: You are not eligible to work.


# 5️⃣ Nested if–else example
marks = 75
if marks >= 90:
    print(" Grade: A+")
else:
    if marks >= 70:
        print(" Grade: B")
    else:
        print(" Grade: C or below")

# Output: Grade: B


# 6️⃣ Using if–else with boolean values
is_sunny = False
if is_sunny:
    print(" Let's go for a walk!")
else:
    print(" Let's stay indoors today.")

# Output: Let's stay indoors today.


# 7️⃣ if–else with membership check
fruits = ["apple", "banana", "mango"]
if "orange" in fruits:
    print(" Orange is in the list.")
else:
    print(" Orange is not in the list.")

# Output: Orange is not in the list.


# 8️⃣ Multiple variable comparison
x = 5
y = 10
if x > y:
    print(" x is greater than y")
else:
    print(" x is smaller than or equal to y")

# Output: x is smaller than or equal to y


# 9️⃣ if–else with user age check
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print(" You are not eligible to vote yet.")

# Example: input 16 → Output: You are not eligible to vote yet


# 🔟 Short-hand if–else example
a = 10
b = 20
print("🔟 a is greater") if a > b else print("🔟 b is greater")

# Output: b is greater
