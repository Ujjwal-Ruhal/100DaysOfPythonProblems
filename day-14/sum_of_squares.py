n = int(input("Enter a number: "))

steps = []
total = 0

for i in range(1, n + 1):
    steps.append(f"{i}²")
    total += i ** 2

print(f"{' + '.join(steps)} = {total}")
