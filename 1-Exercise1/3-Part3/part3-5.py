age = int(input("Please input your age: "))

if (age != 0):
    salary = float(input("Please input your salary: "))

if ((age > 30) and (salary >= 50000)):
    loan = 100000
elif ((age >= 30) and (salary >= 35000)):
    loan = 75000
elif ((age >= 21) and (salary >= 21000)):
    loan = 50000
else:
    print("No loan can be made!")

print(f'Your age = {age} and salary = {salary}, your loan will be {loan}')
