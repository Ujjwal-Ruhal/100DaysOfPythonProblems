try:
    marks = int(input("Enter your marks: "))
    attendance = int(input("Enter your attendance: "))

    if not (0 <= marks <= 100 and 0 <= attendance <= 100):
        print("Invalid Input")
    else:
        final_score = (marks * 0.8) + (attendance * 0.2)
        
        if final_score >= 90:
            grade = "A+"
        elif final_score >= 80:
            grade = "A"
        elif final_score >= 70:
            grade = "B"
        elif final_score >= 60:
            grade = "C"
        elif final_score >= 50:
            grade = "D"
        else:
            grade = "Fail"

        print(f"Final Score: {final_score:.2f}")
        print(f"Grade: {grade}")

except ValueError:
    print("Invalid Input")
