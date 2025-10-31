num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    factorial = 1
    steps = []

    for i in range(num, 0, -1):
        factorial *= i
        steps.append(str(i))

    if num == 0:
        print("0! = 1")
    else:
        print(" x ".join(steps), "=", factorial)
