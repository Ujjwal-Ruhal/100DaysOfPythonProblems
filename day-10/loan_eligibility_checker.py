try:
    age = int(input("Enter your age: "))
    income = int(input("Enter your monthly income: "))
    credit_score = int(input("Enter your credit score: "))
    existing_loan = input("Do you have an existing loan (y/n): ").strip().lower()

    if age < 0 or income < 0 or credit_score < 0 or existing_loan not in ['y', 'n']:
        print("Invalid Input")

    elif not (21 <= age <= 60):
        print("Not eligible due to age limit")

    elif not (300 <= credit_score <= 900):
        print("Invalid credit score range")

    elif credit_score >= 700:
        if existing_loan == 'y' and income >= 40000:
            print("Eligible for loan")
        elif existing_loan == 'n' and income >= 25000:
            print("Eligible for loan")
        else:
            print("Not eligible due to low income")
    else:
        print("Not eligible due to low credit score")

except ValueError:
    print("Invalid Input")
