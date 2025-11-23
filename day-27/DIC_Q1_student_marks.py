student_info = {}

try:
    entities = int(input("How many students? "))

    for i in range(entities):
        name = input("Enter student name: ").strip()

        # if name already exists → prevent overwriting
        if name in student_info:
            print("Name already exists. Try a different name!")
            continue

        marks = int(input("Enter marks: "))
        
        # basic validation
        if marks < 0 or marks > 100:
            print("Invalid marks. Must be between 0-100.")
            continue
        
        student_info[name] = marks

    print("\nFinal Student Info:", student_info)

except ValueError:
    print("Invalid input! Please enter correct values.")
