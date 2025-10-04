a = float(input("Enter the Amount: "))
r = float(input("Enter the Rate (%): "))
t = float(input("Enter the Time (years): "))

simple_interest = (a * r * t) / 100
total_amount = a + simple_interest

print(f"Simple Interest: {simple_interest:.2f}")
print(f"Total Amount after {t} years: {total_amount:.2f}")
