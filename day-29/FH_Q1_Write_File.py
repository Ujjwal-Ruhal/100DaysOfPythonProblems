with open("note.txt", "a") as file:
    text = input("Write something: ")
    file.write(text + "\n")
    print("Saved to file!")

with open("note.txt", "r") as file:
    print("\nCurrent file content:")
    print(file.read())