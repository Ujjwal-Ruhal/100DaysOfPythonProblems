'''
Python Data Types
Data types in Python are a way to classify data items. They represent the kind of value, which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.

The following are standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview
'''
'''
Below code assigns variable 'x' different values of few Python data types - int, float, list, tuple and string. Each assignment replaces previous value, making 'x' take on data type and value of most recent assignment.
'''

x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {1:24 , 2:'hello', 'name':'ujjwal','age':20.1} # dict- key:value

'''Numeric Data Types
Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating number or even a complex number. These values are defined as int, float and complex classes.

Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). There is no limit to how long an integer value can be.
Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, character e or E followed by a positive or negative integer may be appended to specify scientific notation.
Complex Numbers: It is represented by a complex class. It is specified as (real part) + (imaginary part)j. For example - 2+3j
'''
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

'''
 Sequence Data Types
A sequence is an ordered collection of items, which can be of similar or different data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

String Data Type
Python Strings are arrays of bytes representing Unicode characters. In Python, there is no character data type, a character is a string of length one. It is represented by str class.

Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.
'''
