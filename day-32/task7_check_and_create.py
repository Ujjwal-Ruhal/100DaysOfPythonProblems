import os

file_name = input("Enter file name: ")

if os.path.exists(file_name):
    print("File already exists.")
else:
    with open(file_name, "w") as f:
        f.write("This is a new file created by the program.\n")
    print(f"File '{file_name}' created successfully.")
