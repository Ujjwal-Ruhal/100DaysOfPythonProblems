# -------------------------------
# FUNCTION EXAMPLES IN PYTHON
# -------------------------------

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
print("*****")  # Separator


# -------------------------------
# PASSING FUNCTION AS ARGUMENT
# -------------------------------

# Define a function that says hello
def greet_func():
    print("Hello, Ujjwal!")

# Define another function that takes a function as an argument
def call_function(func):
    print("Calling the function you passed...")
    func()  # executes the function you passed

# Pass 'greet_func' function to 'call_function'
call_function(greet_func)
print("*****")  # Separator


# Example with multiple math functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(func, x, y):
    result = func(x, y)
    print("Result:", result)

# Pass different functions as arguments
calculate(add, 5, 3)
calculate(multiply, 5, 3)
print("*****")  # Separator


# -------------------------------
# FUNCTION RETURNING ANOTHER FUNCTION
# -------------------------------

def outer():
    def inner():
        print("Inner function executed!")
    return inner  # returning function

# Get the returned function
new_func = outer()

# Call the inner function
new_func()
print("*****")  # Separator


# -------------------------------
# APPLYING A FUNCTION TO A LIST
# -------------------------------

def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, values):
    result = []
    for v in values:
        result.append(func(v))
    return result

numbers = [1, 2, 3, 4]

print("Squares:", apply_function(square, numbers))
print("Cubes:", apply_function(cube, numbers))
print("*****")  # Final separator
