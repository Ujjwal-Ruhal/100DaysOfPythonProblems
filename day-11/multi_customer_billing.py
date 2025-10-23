try:
    num = int(input("Enter number of customers: "))

    if num > 0:
        for i in range(1, num + 1):
            print(f"\n--- Customer {i} ---")
            try:
                unit = int(input("Enter units consumed: "))

                if unit >= 0:
                    if unit <= 100:
                        total_bill = (unit * 5) + 50
                    elif unit <= 200:
                        total_bill = ((unit - 100) * 7) + 550
                    elif unit <= 300:
                        total_bill = ((unit - 200) * 10) + 1250
                    else:
                        total_bill = ((unit - 300) * 15) + 2250

                    if total_bill > 2000:
                        total_bill += total_bill * 0.05

                    print(f"Total Bill: ₹{total_bill:.2f}")
                else:
                    print("Invalid Input (Units cannot be negative)")
            except ValueError:
                print("Invalid Input (Please enter a number)")

            print("-" * 30)
    else:
        print("Invalid Input (Customer count must be positive)")

except ValueError:
    print("Invalid Input (Please enter a number)")
