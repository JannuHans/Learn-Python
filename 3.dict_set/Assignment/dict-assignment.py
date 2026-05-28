# dictionary assignment 19th may

students = {
    "Rahul" : 85,
    "Sneha" : 67,
    "Amit" : 67,
    "John" : 45
}

#Find topper
topper = max(students, key =students.get)
print(topper, students[topper])

#Find failed students (<50)
for x, y in students.items():
    if y < 50:
        print(x,y)



#Find students with same marks
for student1,marks1 in students.items():
    for student2, marks2 in students.items():
        if student1 != student2 and marks1 == marks2:
            print(student1,student2,marks1)


# OR

same_marks={}
for student,marks in students.items():
    if marks not in same_marks:
        same_marks[marks] = [student]
    else:
        same_marks[marks].append(student)

for marks, student in same_marks.items():
    if len(student)>1:
        print(marks,student)

#Print grades
grades={}
for x,y in students.items():
    if y <= 100 and y > 80:
        grades[x] = "A"
    elif y <= 80 and y > 60:
        grades[x] = "B"
    else:
        grades[x] = "C"

for x in grades.items():
    print(x)


#Merge Dictionaries
d1 = {
    "a":1,
    "d":3
}

d2 = {
    "c":2,
    "b":4
}

d1.update(d2)
print(d1)

sort1 = dict(sorted(d1.items()))
print(sort1)

so = dict(sorted(d1.items()))

sort2 = dict(sorted(d1.items(), key=lambda item: item[1]))

print(sort2)

#Shopping Cart System
cart = {
    "Laptop" : {"price":5000,
                "qty":1
                },
    "Mouse" : {"price":500,
               "qty":2
               }
}

#Add product
cart["keyboard"] = {"price":700,"qty":1}
print(cart)

#Update quantity
cart["Laptop"]["qty"] = 3
print(cart)

#Remove product
cart.pop("Mouse")
print(cart)

#Calculate total bill
total=0
for x,y in cart.items():
    total +=y ["price"]*y["qty"]

print(total)

#Find most expensive product
max_product = max(cart, key=lambda p: cart[p]["price"])
print(max_product)

#Apply 10% discount if total > 50000
if total > 50000:
    discount = total * 0.10
    final_bill = total - discount

    print(final_bill)

else:
    print(total)