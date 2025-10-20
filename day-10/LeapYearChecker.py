try:
    year = int(input("Enter year: "))
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    print(f"{year} is leap year: {leap}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
