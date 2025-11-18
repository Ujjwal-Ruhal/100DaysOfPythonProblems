# input as a string
user_input = input("Enter numbers separated by comma: ")

# convert to tuple
numbers = tuple(x.strip() for x in user_input.split(","))

# but if you are fill input as a integer type 
# to use -> numbers = tuple(int(x.strip()) for x in user_input.split(","))

# reverse tuple
new_tup = numbers[::-1]

print(f"Original tuple : {numbers}")
print(f"Reversed tuple : {new_tup}")
