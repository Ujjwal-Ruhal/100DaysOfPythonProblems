'''
Python Data Types

Data types in Python classify data items — they define the kind of value and what operations
can be performed on it. Since everything in Python is an object, data types are classes,
and variables are instances (objects) of these classes.

Standard Built-in Data Types in Python:
1. Numeric: int, float, complex
2. Sequence: str, list, tuple
3. Mapping: dict
4. Boolean: bool
5. Set: set, frozenset
6. Binary: bytes, bytearray, memoryview
'''

# =====================================================
# Demonstrating different data types with unique variables
# =====================================================

# Assigning different data types to separate variables
x_int = 50                             # int
x_float = 60.5                         # float
x_str = "Hello World"                  # string
x_list = ["Hello", "for", "Hello"]     # list 
x_tuple = ("Hello", "for", "Hello")    # tuple
x_dict = {1: 24, 2: 'hello', 'name': 'ujjwal', 'age': 20.1}  # dict

print("\n--- Basic Data Type Assignments ---")
print("Integer:", x_int, "| Type:", type(x_int))     # Output: 50 | <class 'int'>
print("Float:", x_float, "| Type:", type(x_float))   # Output: 60.5 | <class 'float'>
print("String:", x_str, "| Type:", type(x_str))      # Output: Hello World | <class 'str'>
print("List:", x_list, "| Type:", type(x_list))      # Output: ['Hello', 'for', 'Hello'] | <class 'list'>
print("Tuple:", x_tuple, "| Type:", type(x_tuple))   # Output: ('Hello', 'for', 'Hello') | <class 'tuple'>
print("Dictionary:", x_dict, "| Type:", type(x_dict))
# Output: {1: 24, 2: 'hello', 'name': 'ujjwal', 'age': 20.1} | <class 'dict'>


# =====================================================
# NUMERIC DATA TYPES
# =====================================================
'''
Numeric Data Types:
- int: whole numbers (no decimals)
- float: numbers with decimal point
- complex: numbers with real and imaginary parts
'''

print("\n--- Numeric Data Types ---")

a = 5
print(a, "->", type(a))     # Output: 5 -> <class 'int'>

b = 5.0
print(b, "->", type(b))     # Output: 5.0 -> <class 'float'>

c = 2 + 4j
print(c, "->", type(c))     # Output: (2+4j) -> <class 'complex'>


# =====================================================
# SEQUENCE DATA TYPES
# =====================================================
'''
Sequence Types in Python include: string, list, and tuple.
They are ordered collections that can be indexed and iterated.
'''

# -------------------------
# STRING DATA TYPE
# -------------------------
print("\n--- String Data Type ---")

s = 'Welcome to the Ujjwal'
print("String:", s)          # Output: Welcome to the Ujjwal
print("Type:", type(s))      # Output: <class 'str'>

# Accessing characters by index
print("s[1]:", s[1])         # Output: e
print("s[2]:", s[2])         # Output: l
print("s[-1]:", s[-1])       # Output: l


# -------------------------
# LIST DATA TYPE
# -------------------------
print("\n--- List Data Type ---")

# Lists are mutable and ordered collections
a = [1, 2, 3]
b = ["Hello", "For", "Hello", 4, 5]

print("List a:", a)          # Output: [1, 2, 3]
print("List b:", b)          # Output: ['Hello', 'For', 'Hello', 4, 5]

# Accessing elements
print("a[0]:", a[0])         # Output: 1
print("a[2]:", a[2])         # Output: 3
print("a[-1]:", a[-1])       # Output: 3 (last element)
print("a[-3]:", a[-3])       # Output: 1 (first element)


# -------------------------
# TUPLE DATA TYPE
# -------------------------
print("\n--- Tuple Data Type ---")

# Tuples are ordered but immutable
tup1 = ()
tup2 = ('Hello', 'For')
print("Tuple 1:", tup1)      # Output: ()
print("Tuple 2:", tup2)      # Output: ('Hello', 'For')

# Tuple from list
tup3 = tuple([1, 2, 3, 4, 5])
print("Tuple 3:", tup3)      # Output: (1, 2, 3, 4, 5)

# Accessing tuple elements
print("tup3[0]:", tup3[0])   # Output: 1
print("tup3[-1]:", tup3[-1]) # Output: 5
print("tup3[-3]:", tup3[-3]) # Output: 3


# =====================================================
# BOOLEAN DATA TYPE
# =====================================================
'''
Boolean Data Type:
Represents one of two values: True or False.
Often used in conditional statements.
'''

print("\n--- Boolean Data Type ---")
print("Type of True:", type(True))     # Output: <class 'bool'>
print("Type of False:", type(False))   # Output: <class 'bool'>

# Demonstration with expressions
print("Is 10 > 5?", 10 > 5)            # Output: True
print("Is 3 == 7?", 3 == 7)            # Output: False


# =====================================================
# SET DATA TYPE
# =====================================================
'''
Set Data Type:
- Unordered collection with no duplicate elements.
- Mutable and iterable.
- Elements must be immutable (hashable).
'''

print("\n--- Set Data Type ---")

# Empty set
s1 = set()
print("Empty Set:", s1)  # Output: set()

# From string (duplicates removed)
s1 = set("HelloUjjwalHello")
print("Set from String:", s1)

# From list (duplicates removed)
s2 = set(["Hello", "For", "Hello"])
print("Set from List:", s2)  # Output: {'Hello', 'For'}

# Looping through a set
print("Looping through set:")
for i in s2:
    print(i, end=" ")   # Output: Hello For (order may vary)
print()

# Check membership
print("'Hello' in s2?", "Hello" in s2)  # Output: True


# =====================================================
# DICTIONARY DATA TYPE
# =====================================================
'''
Dictionary:
- Key-value pairs.
- Keys must be unique and immutable.
- Values can be of any data type.
'''

print("\n--- Dictionary Data Type ---")

# Empty dictionary
d = {}

# Creating dictionary directly
d = {1: 'Hello', 2: 'For', 3: 'Hello'}
print("Dictionary d:", d)

# Creating using dict() constructor
d1 = dict({1: 'Hello', 2: 'For', 3: 'Hello'})
print("Dictionary d1:", d1)

# Accessing values
d = {1: 'Hello', 'name': 'Ujjwal', 3: 'Hello'}
print("d['name']:", d['name'])  # Output: Ujjwal
print("d.get(3):", d.get(3))    # Output: Hello
