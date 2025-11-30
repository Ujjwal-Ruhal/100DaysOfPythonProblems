source = "task1.txt"

destination = "task5_copy.txt"

with open(source, "r") as src, open(destination, "w") as dest:
    for line in src:
        dest.write(line)

print(f"File copied from {source} to {destination} successfully.")