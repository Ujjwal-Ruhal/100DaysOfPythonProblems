file_path = "task1.txt"

word_count = 0

with open(file_path, "r") as f:
    for line in f:
        words = line.split()
        word_count += len(words)

print("Total words:", word_count)
