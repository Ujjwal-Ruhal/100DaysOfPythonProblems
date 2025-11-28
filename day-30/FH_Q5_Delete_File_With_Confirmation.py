import os

filename = input("Enter file name (e.g., xyz.txt): ").strip()

if os.path.exists(filename):

    confirm = input(f"Are you sure you want to delete '{filename}'? (Y/N): ").strip().lower()

    if confirm in ("y", "yes"):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print("Delete operation cancelled.")

else:
    print("Error: File does not exist.")
