import os

file_name = input("Enter new file name (example: myfile.txt): ").strip()

# check if file already exists
if os.path.exists(file_name):
    print("File already exists!")

    choice = input("Do you want to overwrite it? (Y/N): ").strip().lower()

    if choice == "y":
        with open(file_name, "w") as f:
            content = input("Write content for the file: ")
            f.write(content + "\n")
        print("File overwritten successfully!")

    else:
        print("Operation cancelled.")

# if file does NOT exist → create new file
else:
    with open(file_name, "w") as f:
        content = input("Write content for the new file: ")
        f.write(content + "\n")
    print("New file created successfully!")
