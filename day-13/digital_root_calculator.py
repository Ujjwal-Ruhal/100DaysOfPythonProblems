# digital_root_calculator.py

try:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        print("Invalid Input: Only positive numbers are allowed.")
    else:
        step = 1
        while num >= 10:
            digits = [int(d) for d in str(num)]
            total = sum(digits)
            steps_str = '+'.join(str(d) for d in digits)
            print(f"Step {step}: {steps_str} = {total}")
            num = total
            step += 1

        print(f"Final Result: {num}")
except ValueError:
    print("Invalid Input: Please enter a valid integer.")
