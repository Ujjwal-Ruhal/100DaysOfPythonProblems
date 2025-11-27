# Q2 — Write lines to file until user enters STOP

file_name = "save_text.txt"

# Write until STOP
with open(file_name, "a") as file:
    while True:
        text = input("Write something: ")

        if text.lower() == "stop":
            break

        file.write(text + "\n")
        print("Saved.")

# Read stored content
with open(file_name, "r") as file:
    print("\nCurrent file content:")
    print(file.read())
