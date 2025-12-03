import csv
import os
import sys

def ask_nonempty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input cannot be empty. Try again.")

def ask_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter a number.")
            continue
        if not s.isdigit():
            print("Invalid number. Enter a positive integer.")
            continue
        n = int(s)
        if n <= 0:
            print("Number must be greater than zero.")
            continue
        return n

def valid_email(email):
    # Basic email validation
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True

def ask_valid_email(prompt):
    while True:
        e = input(prompt).strip()
        if not e:
            print("Email cannot be empty.")
            continue
        if valid_email(e):
            return e
        print("Invalid email format. Example: user@example.com")

def ask_valid_age(prompt, min_age=0, max_age=120):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Age cannot be empty.")
            continue
        if not (s.lstrip("-").isdigit()):
            print("Age must be a number.")
            continue
        age = int(s)
        if age < min_age or age > max_age:
            print(f"Age must be between {min_age} and {max_age}.")
            continue
        return age

def main():
    try:
        csv_name = ask_nonempty("Enter CSV file name (without extension): ")
        file_name = csv_name + ".csv"

        if os.path.exists(file_name):
            choice = input(f"File '{file_name}' already exists. Overwrite? (y/n): ").strip().lower()
            if choice != "y":
                print("Operation cancelled. No file written.")
                return

        count = ask_positive_int("How many entries do you want to add? ")

        with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["name", "email", "age"])

            for i in range(1, count + 1):
                print(f"\nEntry {i}/{count}:")
                username = ask_nonempty("  Enter name: ")
                email = ask_valid_email("  Enter email: ")
                age = ask_valid_age("  Enter age: ")

                writer.writerow([username, email, age])

        print(f"\nCSV file '{file_name}' created successfully with {count} records.")

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
