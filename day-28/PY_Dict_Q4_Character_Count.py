'''
Input:  "Hello World"
Output:
{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
'''
def character_count(sentence):
    count_each_character = {}
    
    for character in sentence:
        if character.isspace():
            continue
        count_each_character[character] = count_each_character.get(character, 0) + 1
    
    return count_each_character
        
try:
    user_input = input("Enter your sentence here: ")

    result = character_count(user_input)
    print("The result is : ", result)

except ValueError:
    print("Invalid Input, please try again")
