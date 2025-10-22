try:
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid Input")
    else:
        if units <= 100:
            total_bill = units * 5
        elif units <= 200:
            total_bill = (100 * 5) + ((units - 100) * 7)
        elif units <= 300:
            total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        else:
            total_bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

        total_bill += 50  # fixed charge

        if total_bill > 2000:
            total_bill += total_bill * 0.05  # 5% surcharge

        print(f"Total Bill: ₹{total_bill:.2f}")

except ValueError:
    print("Invalid Input")
