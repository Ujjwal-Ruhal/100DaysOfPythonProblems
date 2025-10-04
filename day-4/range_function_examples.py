# ============================================
# Python range() Function Examples
# ============================================

"""
range() function ka use number sequences generate karne ke liye hota hai.

Syntax:
    range(start, stop, step)

👉 Parameters:
   - start: sequence ka starting number (default = 0)
   - stop: sequence end point (excluded)
   - step: difference between each number (default = 1)

👉 Returns: a sequence of numbers (NOT a list by default)
            But we can convert it to list using list(range(...))
"""

# 1️⃣ Basic example
print("1️⃣ Basic range(5):", list(range(5)))
# Output: [0, 1, 2, 3, 4]
# (starts from 0 and goes up to 4)

# 2️⃣ Range with start and stop
print("2️⃣ range(2, 8):", list(range(2, 8)))
# Output: [2, 3, 4, 5, 6, 7]

# 3️⃣ Range with step value
print("3️⃣ range(1, 10, 2):", list(range(1, 10, 2)))
# Output: [1, 3, 5, 7, 9]

# 4️⃣ Range with negative step (reverse order)
print("4️⃣ range(10, 0, -2):", list(range(10, 0, -2)))
# Output: [10, 8, 6, 4, 2]

# 5️⃣ Using range in for loop
print("5️⃣ Using range() in for loop:")
for i in range(5):
    print("   Number:", i)
# Output: 0 1 2 3 4

# 6️⃣ Using start, stop, step in loop
print("6️⃣ range(2, 12, 3):")
for num in range(2, 12, 3):
    print("   ->", num)
# Output: 2 5 8 11

# 7️⃣ Iterating backward with negative step
print("7️⃣ Counting backward from 10 to 1:")
for x in range(10, 0, -1):
    print(x, end=" ")
print()

# 8️⃣ Using range() with len()
fruits = ["apple", "banana", "mango", "orange"]
print("\n8️⃣ Using range with len():")
for i in range(len(fruits)):
    print(f"   Index {i} = {fruits[i]}")

# Output:
# Index 0 = apple
# Index 1 = banana
# Index 2 = mango
# Index 3 = orange

# 9️⃣ range() object is iterable
r = range(5)
print("\n9️⃣ Type of range object:", type(r))
print("   Converted to list:", list(r))

# Output:
# <class 'range'>
# [0, 1, 2, 3, 4]

# 🔟 Example: even numbers between 0 to 20
print("\n🔟 Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# 11️⃣ Example: odd numbers between 1 to 20
print("\n1️⃣1️⃣ Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# 12️⃣ Example: range with condition
print("\n1️⃣2️⃣ Multiples of 3 between 1 and 30:")
for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")
print()

# 🧠 Summary
"""
✅ range() number sequence banata hai.
✅ Default start = 0, step = 1 hota hai.
✅ range(stop) → 0 se (stop-1) tak.
✅ range(start, stop) → start se (stop-1) tak.
✅ range(start, stop, step) → har step ke gap ke sath.
✅ Negative step se reverse counting hoti hai.
✅ range() loops me bahut use hota hai.
"""

print("\n✅ End of range() function examples.")
