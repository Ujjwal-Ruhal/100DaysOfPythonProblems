file_path = "task1.txt"

longest = ""

with open(file_path, "r") as f:
    for line in f:
        words = line.split()
        for w in words:
            if len(w) > len(longest):
                longest = w

print("Longest word:", longest)
print("Length:", len(longest))
