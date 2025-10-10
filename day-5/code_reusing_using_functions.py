# Function that prints whatever fruit name user enters
def fruit_name():
    name = input("Enter a fruit name: ")
    print("You entered:", name)

# Function call
fruit_name()

print("*****")  # Separator


# Function with a parameter
def greet(name):
    print("Hello", name)

# Function call with argument
greet("Ujjwal")

print("*****")  # Separator


# Function that returns a full name
def full_name(first, last):
    return first + " " + last

# Function call and store the returned value
name = full_name("Ujjwal", "Ruhal")

# Print result
print("Your full name is:", name)

print("*****")  # Separator


# Function that multiplies two numbers and returns result
def multiply(a, b):
    return a * b

# Use the returned value
result = multiply(5, 6)
print("Multiplication result is:", result)

print("*****")  # Final separator
