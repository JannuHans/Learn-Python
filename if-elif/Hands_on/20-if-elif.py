#An "if statement" is written by using the if keyword.

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Multiple statements in an if block:
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#The Elif Keyword
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#The Else Keyword
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200

if b > a:
  pass


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