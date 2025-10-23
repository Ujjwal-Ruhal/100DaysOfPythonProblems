try:
    salary = float(input("Enter salary: "))
    experience = float(input("Enter experience (in years): "))
    rating = float(input("Enter rating (0-5): "))

    if not (salary > 0 and experience >= 0 and 0 <= rating <= 5):
        print("Invalid Input")
    else:
        bonus = 0

        if experience >= 10:
            bonus = (salary * (20 if rating >= 4.5 else 15 if rating >= 3 else 0)) / 100
        elif experience >= 5:
            bonus = (salary * (15 if rating >= 4.5 else 10 if rating >= 3 else 0)) / 100
        else:
            bonus = (salary * (10 if rating >= 4.5 else 5 if rating >= 3 else 0)) / 100

        if bonus == 0:
            print("No bonus due to rating")
        else:
            print(f"Bonus: ₹{bonus:.2f}\nTotal Salary: ₹{salary + bonus:.2f}")
except ValueError:
    print("Invalid Input")
