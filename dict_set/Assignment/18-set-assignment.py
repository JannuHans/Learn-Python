#Sets assignment

#Part 1

python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

#1.Students in both Python and SQL
student1 = python_students & sql_students
print("Students in both Python and SQL:", student1)

#Students in all 3 courses
student2 = python_students & sql_students & aws_students
print("Students in all 3 courses:", student2)   

#Students only in Python
student3 = python_students - (sql_students | aws_students)
print("Students only in Python:", student3)

#Total unique students
student4 = python_students | sql_students | aws_students
print("Total unique students:", student4)

#Students not enrolled in AWS
student5 = student4 - aws_students
print("Students not enrolled in AWS:", student5)

#Students in more than 2 courses.
student6 = (python_students & sql_students) | (python_students & aws_students) | (sql_students & aws_students)
print("Students in more than 2 courses:", student6)

#Students whose name starts with 'Ra'
student7 = {s for s in student4 if s.startswith("Ra")}
print("Students whose name starts with 'Ra':", student7)

#Students whose name ends with 'na' or 'an'
student8 = {s for s in student4 if s.endswith("na") or s.endswith("an")}
print("Students whose name ends with 'na' or 'an':", student8)


#Part 2

data = [1,2,2,3,4,4,4,5]

#unique values
unique_values = set(data)
print("Unique values:", unique_values)

#duplicate values
duplicates = set()

for i in data:
    if data.count(i) > 1:
        duplicates.add(i)

print("Duplicate values:", duplicates)

#frequency of each value
frequency = {x: data.count(x) for x in set(data)}
print("Frequency of each value:", frequency)