try:
    sales = float(input("Enter monthly sales: "))
    target = float(input("Enter monthly target: "))
    rating = float(input("Enter customer satisfaction rating (0-5): "))
    salary = float(input("Enter your annual salary: "))

    if not (sales > 0 and target > 0 and (0 <= rating <= 5) and salary > 0):
        print("Invalid input: Please enter positive values and rating between 0–5.")
    else:
        sales_percentage = (sales / target) * 100

        # Default values
        grade = "D"
        bonus = 0

        if sales_percentage >= 120 and rating >= 4.5:
            grade, bonus = "A+", (salary * 25) / 100
        elif sales_percentage >= 100 and rating >= 4:
            grade, bonus = "A", (salary * 20) / 100
        elif sales_percentage >= 90 and rating >= 3.5:
            grade, bonus = "B", (salary * 10) / 100
        elif sales_percentage >= 75 and rating >= 3:
            grade, bonus = "C", (salary * 5) / 100

        # Loyalty bonus for top performers with high salary
        if salary > 1000000 and grade in ("A+", "A"):
            bonus += bonus * 0.05

        total_salary = salary + bonus

        print("\n" + "*" * 35)
        print(f"Sales Percentage : {sales_percentage:.2f}%")
        print(f"Grade            : {grade}")
        print(f"Bonus            : ₹{bonus:.2f}")
        print(f"Total Salary     : ₹{total_salary:.2f}")
        print("*" * 35)

except ValueError:
    print("Invalid input: Please enter numeric values only.")
except ZeroDivisionError:
    print("Division by zero error: Target cannot be zero.")
