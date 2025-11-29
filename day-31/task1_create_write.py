file_path = "task1.txt"

lines = [
    "This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4",
    "This is line 5"
]

with open(file_path, "w") as f:
    for line in lines:
        f.write(line + "\n")

print("5 lines written to task1.txt successfully!")
