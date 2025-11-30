import os

file_name = input("Enter the file name to delete: ")

if os.path.exists(file_name):
    choice = input("Are you sure you want to delete this file? (y/n): ").lower()
    
    if choice == "y":
        os.remove(file_name)
        print("File deleted successfully.")
    else:
        print("Delete operation cancelled.")
else:
    print("File not found.")
