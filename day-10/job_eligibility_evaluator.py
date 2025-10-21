try:
    age = int(input("Enter age: "))
    qualification = input("Enter qualification: ").strip().upper()
    experience = int(input("Enter experience (in years): "))
    skills = input("Enter skills (comma separated): ").strip().upper()

    required_qualification = ['BTECH', 'MCA', 'BCA', 'BSC']
    required_skills = ('PYTHON', 'JAVA', 'C++', 'DJANGO', 'FLASK')

    if age <= 0 or experience < 0:
        print("Invalid Input")
    elif qualification not in required_qualification:
        print("Not eligible due to qualification")
    else:
        skill_list = [s.strip().upper() for s in skills.split(',')]
        has_required_skill = any(skill in required_skills for skill in skill_list)

        if not has_required_skill:
            print("No technical skills provided")
        elif (21 <= age <= 35 and experience >= 2) or (age > 35 and experience >= 5):
            if age > 35:
                print("Eligible for job (Experienced Candidate)")
            else:
                print("Eligible for job")
        elif experience < 2:
            print("Not eligible (Not enough experience)")
        else:
            print("You are not eligible due to age")

except ValueError:
    print("Invalid Input")
