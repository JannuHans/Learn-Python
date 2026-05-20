#More Logical Questions
#1. Salary Bonus System
# salary > 50000 → bonus 20%
# salary > 30000 → bonus 10%
# else → bonus 5%

salary = int(input("Enter salary: "))

if salary > 50000:
    bonus = salary * 0.20
elif salary > 30000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus:", bonus)


#4. Divisibility Checker
# check
# divisible by both 3 and 5
# only 3
# only 5
# neither

num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible")


#Create an Employee Management System

# EMPLOYEE DATA
employees = {
    "Jannu": {
        "salary": 50000,
        "department": "IT",
        "experience": 2
    },

    "Ashu": {
        "salary": 85000,
        "department": "AI",
        "experience": 6
    },

    "Abhay": {
        "salary": 40000,
        "department": "HR",
        "experience": 1
    }
}


# TUPLE
company_info = ("UBI Company", "Lucknow")

print("Company:", company_info[0])
print("Location:", company_info[1])


# ADD EMPLOYEE

employees["Aayush"] = {
    "salary": 70000,
    "department": "HR",
    "experience": 5
}

print(employees)


# UPDATE SALARY

employees["Jannu"]["salary"] += 5000
print(employees["Jannu"]["salary"])


# REMOVE EMPLOYEE

del employees["Ashu"]
print(employees)


# HIGHEST SALARY EMPLOYEE

highest = max(
    employees,
    key=lambda emp: employees[emp]["salary"]
)
print(highest)
print("Salary:", employees[highest]["salary"])


# AVERAGE SALARY

total = 0

for details in employees.values():
    total += details["salary"]

average = total / len(employees)

print("Average Salary:", average)


# EXPERIENCE GREATER THAN 3


for emp, details in employees.items():

    if details["experience"] > 3:
        print(emp)


# GRADE SYSTEM

for emp, details in employees.items():

    salary = details["salary"]

    if salary >= 80000:
        grade = "A"

    elif salary >= 50000:
        grade = "B"

    else:
        grade = "C"

    print(emp, "-> Grade", grade)


# SET

departments = []

for details in employees.values():
    departments.append(details["department"])

unique_departments = set(departments)
print(unique_departments)