source = "task1.txt"
destination = "task9_reverse.txt"

with open(source, "r") as f:
    lines = f.readlines()  # list of all lines

# Reverse entire content (lines reversed + text reversed)
reversed_lines = [line[::-1] for line in lines[::-1]]

with open(destination, "w") as f:
    f.writelines(reversed_lines)

print(f"Reversed content written to {destination}")
