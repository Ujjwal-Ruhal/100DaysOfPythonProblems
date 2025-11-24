student_info = {}

try:
    entities = int(input("How many students? "))

    for i in range(entities):
        name = input("Enter student name: ").strip()

        # prevent duplicate keys
        if name in student_info:
            print("Name already exists. Try a different name!")
            continue

        marks = int(input("Enter marks: "))
        if marks < 0 or marks > 100:
            print("Invalid marks. Must be between 0-100.")
            continue

        age = int(input("Enter age: "))
        if age <= 0 or age > 50:
            print("Invalid age, please enter valid age.")
            continue

        # grade logic
        if marks > 90:
            grade = "A"
        elif marks > 80:
            grade = "B"
        elif marks > 60:
            grade = "C"
        elif marks > 33:
            grade = "D"
        else:
            grade = "Fail"

        # store properly
        student_info[name] = {
            "marks": marks,
            "age": age,
            "grade": grade
        }

    print("\nFinal Student Info:", student_info)

except ValueError:
    print("Invalid input! Please enter correct values.")
