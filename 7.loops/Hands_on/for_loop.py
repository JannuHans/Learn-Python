# 1. FOR LOOP

# A for loop is used when we know:

# how many times to repeat
# or when iterating through a collection (list, string, tuple, etc.)

# for variable in sequence:
    # code


for i in range(5):
    print(i)


#range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

#Reverse Loop
for i in range(10, 0, -1):
    print(i)


#Loop Through List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

#Loop Through String
name = "Kavir"
for ch in name:
    print(ch)

#Using len()
numbers = [10, 20, 30]
for i in range(len(numbers)):
    print(i, numbers[i])

#Nested FOR Loop
for i in range(3):
    for j in range(2):
        print(i, j)

#break Statement
#Stops loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)

#continue Statement
#Skips current iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)


#Sum of Numbers
total = 0

for i in range(1, 6):
    total += i

print(total)