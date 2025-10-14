'''
==========================================================
SUPPORTED DATA TYPES AND WHAT THEY CAN STORE (with examples)
==========================================================
'''

print("\n--- 1️⃣  int (Integer) ---")
# int → Stores only whole numbers (positive, negative, or zero)
a = 10
b = -5
c = 0
print(a, b, c)  # Output: 10 -5 0
print(type(a))  # Output: <class 'int'>


print("\n--- 2️⃣  float (Floating-point) ---")
# float → Stores decimal or fractional numbers
x = 3.14
y = -9.8
z = 2e3  # scientific notation = 2000.0
print(x, y, z)  # Output: 3.14 -9.8 2000.0
print(type(x))  # Output: <class 'float'>


print("\n--- 3️⃣  complex (Real + Imaginary) ---")
# complex → stores numbers with real and imaginary parts
comp1 = 2 + 3j
comp2 = 5 - 4j
print(comp1, comp2)  # Output: (2+3j) (5-4j)
print("Real part:", comp1.real, "Imaginary part:", comp1.imag)
print(type(comp1))  # Output: <class 'complex'>


print("\n--- 4️⃣  str (String) ---")
# str → Sequence of characters (letters, digits, symbols)
text1 = "Ujjwal"
text2 = 'Python123!'
text3 = """Multi-line
String Example"""
print(text1)
print(text2)
print(text3)
print(type(text1))  # Output: <class 'str'>


print("\n--- 5️⃣  list (Mutable Sequence) ---")
# list → Ordered, can contain *different data types*, mutable
my_list = [10, "Hello", 3.14, True, [1, 2, 3]]
print(my_list)
# You can modify a list
my_list[0] = 99
print("Modified list:", my_list)
print(type(my_list))  # Output: <class 'list'>


print("\n--- 6️⃣  tuple (Immutable Sequence) ---")
# tuple → Ordered, can contain *different data types*, immutable
my_tuple = (10, "Ujjwal", 2.5, False)
print(my_tuple)
# Trying to modify tuple -> will cause error if uncommented
# my_tuple[0] = 100
print(type(my_tuple))  # Output: <class 'tuple'>


print("\n--- 7️⃣  set (Unordered Unique Collection) ---")
# set → Unordered, unique, mutable (but elements must be immutable)
my_set = {10, "Hello", 3.14, True, 10, "Hello"}  # Duplicates auto removed
print(my_set)  # Output may vary in order
# Adding new element
my_set.add("Python")
print("After adding element:", my_set)
print(type(my_set))  # Output: <class 'set'>


print("\n--- 8️⃣  frozenset (Immutable Set) ---")
# frozenset → Same as set but immutable
f_set = frozenset([1, 2, 3, 2, 1])
print(f_set)  # Output: frozenset({1, 2, 3})
# f_set.add(4)  # ❌ will cause error
print(type(f_set))  # Output: <class 'frozenset'>


print("\n--- 9️⃣  dict (Key:Value Pairs) ---")
# dict → Keys must be immutable (str, int, tuple)
#        Values can be any data type (str, list, dict, etc.)
my_dict = {
    "name": "Ujjwal",
    "age": 21,
    "skills": ["Python", "Django", "Flask"],
    1: (10, 20),
    "marks": {"math": 95, "eng": 88}
}
print(my_dict)
print("Access by key:", my_dict["skills"])
print("Nested dict value:", my_dict["marks"]["math"])
print(type(my_dict))  # Output: <class 'dict'>


print("\n--- 🔟  bool (Boolean) ---")
# bool → True or False values (used in logical operations)
a = True
b = False
print(a, b)
print("Is 10 > 5?", 10 > 5)
print("Is 7 == 3?", 7 == 3)
print(type(a))  # Output: <class 'bool'>


print("\n--- 1️⃣1️⃣  bytes / bytearray / memoryview ---")
# Used for handling binary data (e.g., files, images)

# bytes → immutable sequence of bytes
b = bytes([65, 66, 67])  # ASCII: A=65, B=66, C=67
print("Bytes:", b)  # Output: b'ABC'

# bytearray → mutable sequence of bytes
ba = bytearray([65, 66, 67])
ba[0] = 68  # change first byte (A -> D)
print("Bytearray:", ba)  # Output: bytearray(b'DBC')

# memoryview → shared access to byte data
mv = memoryview(b)
print("Memory view of bytes:", mv)
print("First byte value:", mv[0])  # Output: 65
