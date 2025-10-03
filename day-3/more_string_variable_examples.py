# Example 1: Join first name and last name
first_name = "Rahul"
last_name = "Verma"
print("Full name is", first_name + " " + last_name)
# Output: Full name is Rahul Verma


# Example 2: Repeat a festival greeting
festival = "Happy Diwali "
print(festival * 3)
# Output: Happy Diwali Happy Diwali Happy Diwali 


# Example 3: String slicing (extract part of a name)
country = "India"
print(country[0:3])   # First 3 letters
print(country[-2:])   # Last 2 letters
# Output: Ind
#         ia


# Example 4: Length of a string
city = "Hyderabad"
print("Length of city name is", len(city))
# Output: Length of city name is 9


# Example 5: Convert to uppercase and lowercase
food = "samosa"
print(food.upper())   # Output: SAMOSA
print(food.lower())   # Output: samosa


# Example 6: Replace words in a string
sentence = "I love Mumbai"
print(sentence.replace("Mumbai", "Delhi"))
# Output: I love Delhi


# Example 7: Check if a word exists in a string
quote = "Education is the key to success"
print("Education" in quote)   # True
print("Sports" in quote)      # False


# Example 8: Take input and format output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, ", you are", age, "years old.")
# Example Input: Priya, 20
# Output: Hello Priya , you are 20 years old.


# Example 9: Using f-string for better output
actor = "Amitabh"
age = 80
print(f"{actor} is {age} years old.")
# Output: Amitabh is 80 years old.


# Example 10: Print address in multiple lines
address = "House No. 12\nStreet 5\nNew Delhi"
print(address)
# Output:
# House No. 12
# Street 5
# New Delhi
