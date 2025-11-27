import os

src = input("Enter source file: ")
dst = input("Enter destination file: ")

if os.path.exists(src):
    with open(src, "r") as file_1, open(dst, "a") as file_2:
        file_2.write(file_1.read())
    print("Copied successfully!")
else:
    print("Source file not found!")
