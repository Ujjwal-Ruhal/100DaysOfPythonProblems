# sum_even_odd.py

num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid Input")
else:
    even, odd = [], []
    sum_even, sum_odd = 0, 0

    for i in range(1, num + 1):
        if i % 2 == 0:
            even.append(i)
            sum_even += i
        else:
            odd.append(i)
            sum_odd += i

    print("Even Numbers:", *even)
    print("Odd Numbers :", *odd)
    print(f"Sum of Even : {sum_even}")
    print(f"Sum of Odd  : {sum_odd}")
    print(f"Difference  : {abs(sum_even - sum_odd)}")
