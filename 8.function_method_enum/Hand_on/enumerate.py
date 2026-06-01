#3.enumerate() adds an index to each item in an iterable.



# enumerate():
# Used to get both index and value while looping.

# Syntax:
# enumerate(iterable, start=0)
# """

# =========================================
# 1. WITHOUT ENUMERATE
# =========================================

fruits = ["Apple", "Banana", "Mango"]

index = 0

for fruit in fruits:
    print(index, fruit)
    index += 1

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# =========================================
# 2. WITH ENUMERATE
# =========================================

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# =========================================
# 3. STARTING INDEX FROM 1
# =========================================

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 Apple
# 2 Banana
# 3 Mango


# =========================================
# 4. ENUMERATE RETURNS TUPLES
# =========================================

fruits = ["Apple", "Banana", "Mango"]

print(list(enumerate(fruits)))

# Output:
# [(0, 'Apple'), (1, 'Banana'), (2, 'Mango')]


# =========================================
# 5. USING ENUMERATE WITH STRING
# =========================================

name = "JANNU"

for index, char in enumerate(name):
    print(index, char)

# Output:
# 0 J
# 1 A
# 2 N
# 3 N
# 4 U


# =========================================
# 6. USING ENUMERATE WITH TUPLE
# =========================================

numbers = (10, 20, 30)

for index, value in enumerate(numbers):
    print(index, value)

# Output:
# 0 10
# 1 20
# 2 30


# =========================================
# 7. FIND POSITION OF AN ITEM
# =========================================

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    if fruit == "Mango":
        print("Found at index:", index)

# Output:
# Found at index: 2


# =========================================
# 8. NUMBERED LIST
# =========================================

tasks = ["Study", "Practice", "Sleep"]

for num, task in enumerate(tasks, start=1):
    print(f"{num}. {task}")

# Output:
# 1. Study
# 2. Practice
# 3. Sleep


# =========================================
# HANDS-ON PRACTICE
# =========================================

# Q1. Print index and value of a list.

# Q2. Print index and character of a string.

# Q3. Print student names with numbering starting from 1.

# Q4. Find the position of "Python" in a list.

# Q5. Create a numbered menu:
#
# 1. Home
# 2. About
# 3. Contact


# =========================================
# INTERVIEW QUESTIONS
# ==========================================

# Q1. What is enumerate()?
#
# enumerate() adds a counter to an iterable
# and returns index-value pairs.

# Q2. Why use enumerate()?
#
# To get both index and value together
# during iteration.

# Q3. What does enumerate() return?
#
# An enumerate object that produces tuples:
# (index, value)

# Example:
#
# list(enumerate(["A", "B", "C"]))
#
# Output:
# [(0, 'A'), (1, 'B'), (2, 'C')]

# Q4. Can we change the starting index?
#
# Yes
#
# enumerate(data, start=1)

# =========================================
# QUICK REVISION
# ==========================================

# Without enumerate:
#
# index = 0
# for item in data:
#     print(index, item)
#     index += 1

# With enumerate:
#
# for index, item in enumerate(data):
#     print(index, item)

# Most Common Usage:
#
# for i, value in enumerate(my_list):
#     print(i, value)