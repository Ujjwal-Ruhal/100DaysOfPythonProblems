import os

file_name = "save_somthing.txt"

def show_menu():
    print("""
        1) Write (Overwrite file)
        2) Append (Add to file)
        3) Read file
        4) Exit
    """)

while True:
    show_menu()
    
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number only.\n")
        continue
    
    # Option 1: Overwrite
    if user_choice == 1:
        write = input("Write something: ")
        with open(file_name, "w") as file:
            file.write(write + "\n")
        print("File overwritten successfully!\n")
    
    # Option 2: Append
    elif user_choice == 2:
        write = input("Write something: ")
        with open(file_name, "a") as file:
            file.write(write + "\n")
        print("Text appended successfully!\n")
    
    # Option 3: Read File
    elif user_choice == 3:
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name, "r") as file:
                print("\n--- File Content ---")
                print(file.read())
                print("---------------------\n")
        else:
            print("File is empty or does not exist.\n")
    
    # Option 4: Exit
    elif user_choice == 4:
        print("Exiting program... Bye!")
        break
    
    else:
        print("Invalid choice, please choose between 1 to 4.\n")
