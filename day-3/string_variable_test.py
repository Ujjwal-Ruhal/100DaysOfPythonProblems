# Q1: Take a student name and class as input. 
# Print: "<name> is in class <class>"
name = input("Enter student name: ")
class_name = input("Enter class: ")
print(name, "is in class", class_name)
# Example Input: Amit, 10
# Output: Amit is in class 10


# Q2: Store 2 integers in variables x and y. 
# Print their sum, product and difference.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum is", x + y)
print("Product is", x * y)
print("Difference is", x - y)
# Example Input: 12, 5
# Output: Sum is 17
#         Product is 60
#         Difference is 7


# Q3: Slice the word "HIMALAYA" to print "HIA".
word = "HIMALAYA"
print(word[0:3:2])  
# Output: HIA


# Q4: Take a sentence as input and print its first 3 characters.
sentence = input("Enter a sentence: ")
print("First three characters are:", sentence[0:3])
# Example Input: India is great
# Output: Ind


# Q5: Take your city name and print it 4 times.
city = input("Enter your city: ")
print(city * 4)
# Example Input: Delhi
# Output: DelhiDelhiDelhiDelhi


# Q6: Store your favourite actor’s first and last name in two variables. 
# Print full name.
first_name = input("Enter actor's first name: ")
last_name = input("Enter actor's last name: ")
print("Full name is", first_name + " " + last_name)
# Example Input: Shah, Rukh
# Output: Full name is Shah Rukh
