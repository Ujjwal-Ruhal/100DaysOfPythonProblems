# Wrong: This will give SyntaxError because hello world is not inside quotes
# print(hello world)   # SyntaxError: invalid syntax

# Correct: String inside single quotes
print('hello world')  
# Output: hello world

# Wrong: This will give SyntaxError because quotes are mismatched
# print('python's world')   # SyntaxError: unterminated string literal

# Correct: String inside double quotes
print("hello world")  
# Output: hello world

# Correct: Single quote inside double quotes
print("python's world")  
# Output: python's world

# Correct: Escaping single quote using backslash
print('python\'s world')  
# Output: python's world

# Correct: Joining two strings together
print("python's" ' world')  
# Output: python's world

# Correct: Escaping double quotes
print("python's" ' \"world\"')  
# Output: python's "world"

print('python\'s "world"')  
# Output: python's "world"


# Printing a string number (still a string, not an actual number)
print('1')  
# Output: 1

# String concatenation → joining two strings
print('hello' + ' world')  
# Output: hello world

# Repeating string using multiplication
print('python ' * 5)  
# Output: python python python python python 

# Repeating a string number
print(3 * '5 ')  
# Output: 5 5 5 

# Wrong examples that will give errors:
# print('5' * '5')     # Error: Cannot multiply string with string
# print('10' / 2)      # Error: Cannot divide string with integer
# print('5' % 2)       # Error: Wrong use of percent with string
# print('10' / '10')   # Error: Cannot divide string with string

# Printing same text many times with newline
print('I Love You \n' * 10)  
# Output: (prints "I Love You" ten times, each on a new line)

# String concatenation with digits (joined as text, not added)
print('5' + '5')  
# Output: 55

# Printing as plain text (not evaluated as math)
print('1 + 3')  
# Output: 1 + 3

# Single and double quotes
city = "Delhi"
fruit = 'Mango'
print(city)     # Output: Delhi
print(fruit)    # Output: Mango

# String concatenation (joining)
first_name = "Priya"
last_name = "Sharma"
full_name = first_name + " " + last_name
print(full_name)  
# Output: Priya Sharma

# String repetition
greeting = "Namaste "
print(greeting * 3)  
# Output: Namaste Namaste Namaste 

# Escape sequences
print("Hello\nIndia")   # \n = new line
# Output:
# Hello
# India

print("Price:\t50 Rs")  # \t = tab space
# Output: Price:   50 Rs

# String indexing
word = "Python"
print(word[0])   # Output: P
print(word[-1])  # Output: n

# String slicing
print(word[0:3])   # Output: Pyt
print(word[2:])    # Output: thon
