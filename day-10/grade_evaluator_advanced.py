try:
    marks = int(input("Enter your marks : "))
    attendance = int(input("Enter your attendance : "))

    if not 0 <= marks <= 100 and 0 <= attendance <= 100 :
        result = "Invalid Input"
    elif marks >= 90 and attendance >= 90:
        result = "A+"
    elif marks >= 80 and attendance >= 75:
        result = "A"
    elif marks >= 70 and attendance >=60:
        result = "B"
    elif marks >= 60 and attendance >= 50:
        result = "C"
    elif marks >= 50 and attendance >= 40:
        result = "D"
    
    else:
        result = "Fail"
    
    print(f"Grade : {result}")

except ValueError:
    print("Invalid Input")