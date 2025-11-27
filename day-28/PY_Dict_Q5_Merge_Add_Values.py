'''
Input:
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

Output:
{'a': 10, 'b': 25, 'c': 45, 'd': 25}

'''


def merge_dicts(d1, d2):
    merged = d1.copy()  # create a copy so original d1 doesn't change

    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value

    return merged


try:
    # First dictionary input
    user_input1 = input("Enter first dictionary (key:value, comma separated): ")
    d1 = {}
    for pair in user_input1.split(","):
        k, v = pair.split(":")
        d1[k.strip()] = int(v.strip())

    # Second dictionary input
    user_input2 = input("Enter second dictionary (key:value, comma separated): ")
    d2 = {}
    for pair in user_input2.split(","):
        k, v = pair.split(":")
        d2[k.strip()] = int(v.strip())

    # Merge and display
    result = merge_dicts(d1, d2)
    print("\nMerged Dictionary:", result)

except ValueError:
    print("Invalid Input! Please enter values correctly like name:10, marks:5")
