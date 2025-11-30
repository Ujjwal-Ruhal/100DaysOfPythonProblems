file_path = "task1.txt"

vowels = "aeiouAEIOU"
count = 0

with open(file_path, "r") as f:
    for line in f:
        for ch in line:
            if ch in vowels:
                count += 1

print("Total vowels:", count)
