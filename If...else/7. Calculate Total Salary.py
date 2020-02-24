"""
Write a program input Employee name, salary, Designation(m/a/c)
If designation is manager then bonus is 20% on his salary
If designation is analyst then bonus is 10% on his salary
If designation is clerk then bonus is 5% on his salary
Calculate Total Salary.
"""
# Method 1
emp_name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))
desgn = input("Enter designation of an employee (either one of three - m/a/c):")

if desgn == 'm':
    print(emp_name + " is a Manager. Hence Bonus is 20% on his salary. ")
    print("Total salary: ", 0.20*salary + salary)
elif desgn == 'a':
    print(emp_name + " is an analyst. Hence Bonus is 10% on his salary. "+ " ")
    print("Total salary: ", 0.10*salary + salary)
elif desgn == 'c':
    print(emp_name + " is a clerk. Hence Bonus is 20% on his salary. " + "")
    print("Total salary: ", 0.05*salary + salary)
else:
    print("Invalid designation")
    

print("-------------------------------------------------------")

# Method 2
emp_name = input("Enter name: ")
salary = int(input("Enter salary: "))
designation = input("Enter designation (any one m/a/c): ")

if designation == "m":
    bonus = 0.2
elif designation == "a":
    bonus = 0.1
elif designation == "c":
    bonus = 0.05
else:
    bonus = 0
    print("Invalid designation")
    
Total_salary = (salary * bonus) + salary
print("Total Salary: ", Total_salary)

print("-------------------------------------------------------")

# Method 3
emp_name = input("Enter name: ")
salary = int(input("Enter salary: "))
designation = input("Enter designation (any one m/a/c): ")

if designation == "m":
    bonus = 0.2
    if designation == "a":
        bonus = 0.1
    elif designation == "c":
        bonus = 0.05
    total_salary = (salary * bonus) + salary
    print("Total Salary: ", total_salary)
else:
    print("Invalid designation")

    
    
