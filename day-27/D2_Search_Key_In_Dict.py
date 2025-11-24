def search_key(data, key):
    return data.get(key)   # cleaner way


try:
    data = {}
    entities = int(input("How many key-value pairs you want to enter? "))

    for _ in range(entities):
        key = input("Enter key: ").strip()

        if key in data:
            print(" Key already exists! Choose another key.")
            continue     # skip duplicate

        value = input("Enter value: ").strip()
        data[key] = value

    to_find = input("\nEnter key to search: ").strip()
    result = search_key(data, to_find)

    if result is None:
        print("Key not found!")
    else:
        print(f" Value for '{to_find}' is: {result}")

except ValueError:
    print("Invalid Input, try again")
