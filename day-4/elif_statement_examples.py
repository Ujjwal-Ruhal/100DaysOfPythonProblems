# =====================================
# Python 'elif' Statement Examples
# =====================================

"""
'elif' ka matlab hota hai "else if"
Jab ek se zyada conditions check karni ho, tab elif use hota hai.
Program top se bottom tak har condition check karta hai.
Jaisi hi koi condition True milti hai, uske baad ke blocks skip ho jaate hain.
"""

# 1️⃣ Basic if–elif–else example
x = 10
if x > 15:
    print("1️⃣ x is greater than 15")
elif x > 5:
    print("1️⃣ x is greater than 5 but less than or equal to 15")
else:
    print("1️⃣ x is less than or equal to 5")

# Output: x is greater than 5 but less than or equal to 15


# 2️⃣ Grade checking example
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("2️⃣ Grade: A+")
elif marks >= 80:
    print("2️⃣ Grade: A")
elif marks >= 70:
    print("2️⃣ Grade: B")
elif marks >= 60:
    print("2️⃣ Grade: C")
else:
    print("2️⃣ Grade: Fail")

# Example input: 75 → Output: Grade: B


# 3️⃣ Temperature condition example
temperature = 32
if temperature >= 40:
    print("3️⃣ It's a very hot day!")
elif temperature >= 25:
    print("3️⃣ It's a pleasant day.")
elif temperature >= 10:
    print("3️⃣ It's a bit cold.")
else:
    print("3️⃣ It's freezing cold!")

# Output: It's a pleasant day.


# 4️⃣ Multiple range check
age = int(input("Enter your age: "))
if age < 13:
    print("4️⃣ You are a child.")
elif age < 20:
    print("4️⃣ You are a teenager.")
elif age < 60:
    print("4️⃣ You are an adult.")
else:
    print("4️⃣ You are a senior citizen.")

# Example input: 17 → Output: You are a teenager.


# 5️⃣ Check day of the week
day = input("Enter day name: ").lower()
if day == "monday":
    print("5️⃣ Start of the week!")
elif day == "friday":
    print("5️⃣ Weekend is near!")
elif day == "saturday" or day == "sunday":
    print("5️⃣ It's the weekend!")
else:
    print("5️⃣ Just a regular weekday.")

# Example input: sunday → Output: It's the weekend!


# 6️⃣ Nested if–elif example
score = 82
if score >= 90:
    print("6️⃣ Excellent performance!")
elif score >= 70:
    if score >= 80:
        print("6️⃣ Very Good!")
    else:
        print("6️⃣ Good job!")
else:
    print("6️⃣ Keep practicing!")

# Output: Very Good!


# 7️⃣ Comparing three numbers
a = 15
b = 30
c = 25
if a > b and a > c:
    print("7️⃣ a is the largest number")
elif b > a and b > c:
    print("7️⃣ b is the largest number")
else:
    print("7️⃣ c is the largest number")

# Output: b is the largest number


# 8️⃣ Using elif for login check simulation
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("8️⃣ Login successful!")
elif username == "admin":
    print("8️⃣ Password incorrect.")
elif password == "1234":
    print("8️⃣ Username incorrect.")
else:
    print("8️⃣ Both username and password incorrect.")

# Example input: admin / 0000 → Output: Password incorrect.



# Example: + → Result: num1 + num2


# 🔟 Shorthand elif (using chained comparisons)
marks = 68
if 90 <= marks <= 100:
    print("🔟 Excellent!")
elif 75 <= marks < 90:
    print("🔟 Good!")
elif 60 <= marks < 75:
    print("🔟 Average.")
else:
    print("🔟 Needs Improvement.")

# Output: Average.


print("\n✅ End of elif statement examples.")
