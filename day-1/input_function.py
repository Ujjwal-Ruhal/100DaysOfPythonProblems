# Taking a simple string input
name = input("Enter your name: ")
print("Hello", name)  
# Example Input: Ramesh
# Output: Hello Ramesh

# Taking a string input for city
city = input("Enter your city: ")
print("You are from", city)  
# Example Input: Delhi
# Output: You are from Delhi

# Taking an age input (by default input is string)
age = input("Enter your age: ")
print("Your age is", age)  
# Example Input: 21
# Output: Your age is 21

# Converting input to integer for calculation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The total is", num1 + num2)  
# Example Input: 12, 8
# Output: The total is 20

# Converting input to float for decimal numbers
marks1 = float(input("Enter marks of first subject: "))
marks2 = float(input("Enter marks of second subject: "))
print("The total marks are", marks1 + marks2)  
# Example Input: 45.5, 39.5
# Output: The total marks are 85.0

# Demonstrating string concatenation
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your full name is", first_name + " " + last_name)  
# Example Input: Priya, Sharma
# Output: Your full name is Priya Sharma

# Demonstrating string repetition
word = input("Enter a word: ")
count = int(input("How many times to repeat: "))
print("Repeated word is", word * count)  
# Example Input: Namaste, 3
# Output: Repeated word is NamasteNamasteNamaste
