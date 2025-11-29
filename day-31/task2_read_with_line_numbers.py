file_path = "task1.txt"

with open(file_path, "r") as f:
    for index, line in enumerate(f, start=1):
        print(f"{index}: {line.strip()}")
