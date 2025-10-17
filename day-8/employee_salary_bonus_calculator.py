salary = float(input('Base Salary: '))
experience = float(input('Experience: '))
rating = float(input('Rating ( 0 to 5 ) : '))

# my code

if not (salary>0 and (0< rating <=5) and experience>=0):
    print('Invalid Data')
elif not rating>3:
    print('No bonus due to poor performance')
elif experience>=10 and rating>=4.5:
    # if experience >= 10 years, bonus = 15% of base salary and 5% extra bonus if performance rating >= 4.5 . so total bonus = 20%
    bonus = (salary * 20) / 100
    print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')
elif experience>=10 and (3< rating <= 4.5):
    # if experience >= 10 years, bonus = 15% of base salary and if performance not above to 4.5 so no extra bonus
    bonus = (salary * 15) / 100
    print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')
elif experience>=5 and rating>=4.5:
    # if experience >= 5 years, bonus = 10% of base salary and 5% extra bonus if performance rating >= 4.5 . so total bonus = 15%
    bonus = (salary * 15) / 100
    print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')
elif experience>=5 and (3< rating <= 4.5):
    # if experience >= 5 years, bonus = 10% of base salary and if performance not above to 4.5 so no extra bonus
    bonus = (salary * 10) / 100
    print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')
else:
    if experience>=0 and rating>=4.5:
        # if no experience so bonus = 5% of base salary but if performance above to 4.5 so extra bonus 5% are add on to your salary , total bonus = 10%
        bonus = (salary * 10) / 100
        print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')
    else:
        # if no experience so bonus = 5% of base salary but if performance not above to 4.5 so no extra bonus 5% are add on to your salary
        bonus = (salary * 5) / 100
        print(f'Bonus : {bonus}\nTotal Salary : {salary + bonus}')

#  AI Ganerated

bonus = 0

if rating <= 3:
    print('No bonus due to poor performance')
else:
    if experience >= 10:
        bonus = 0.15
    elif experience >= 5:
        bonus = 0.10
    else:
        bonus = 0.05

    if rating >= 4.5:
        bonus += 0.05

    amount = salary * bonus
    print(f'Bonus: {amount}\nTotal Salary: {salary + amount}')
