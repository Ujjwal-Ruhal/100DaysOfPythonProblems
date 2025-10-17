marks = int(input('Enter your marks: '))

if not 0 <= marks <= 100:
    print("Invalid input")
elif marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")
