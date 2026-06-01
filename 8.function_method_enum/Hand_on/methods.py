# 2. Method
# A method is a function that belongs to an object or class.


# PYTHON METHODS

# Function:
# len("hello")

# Method:
# "hello".upper()
# """

# =========================================
# 1. STRING METHODS
# =========================================

name = "jannu"

print(name.upper())      # JANNU
print(name.lower())      # jannu
print(name.capitalize()) # Jannu
print(name.title())      # Jannu

# =========================================
# 2. strip()
# =========================================

text = "   hello   "

print(text.strip())   # Removes spaces from both sides

# =========================================
# 3. replace()
# =========================================

msg = "I like Java"

print(msg.replace("Java", "Python"))

# Output:
# I like Python

# =========================================
# 4. split()
# =========================================

sentence = "Python Java C++"

words = sentence.split()

print(words)

# Output:
# ['Python', 'Java', 'C++']

# =========================================
# 5. join()
# =========================================

languages = ["Python", "Java", "C++"]

result = ", ".join(languages)

print(result)

# Output:
# Python, Java, C++

# =========================================
# 6. startswith() and endswith()
# =========================================

email = "user@gmail.com"

print(email.startswith("user"))
print(email.endswith(".com"))

# Output:
# True
# True

# =========================================
# LIST METHODS
# =========================================

numbers = [10, 20, 30]

# append()
numbers.append(40)
print(numbers)

# Output:
# [10, 20, 30, 40]

# =========================================
# 7. insert()
# =========================================

numbers.insert(1, 15)

print(numbers)

# Output:
# [10, 15, 20, 30, 40]

# =========================================
# 8. remove()
# =========================================

numbers.remove(20)

print(numbers)

# Output:
# [10, 15, 30, 40]

# =========================================
# 9. pop()
# =========================================

numbers.pop()

print(numbers)

# Output:
# [10, 15, 30]

# =========================================
# 10. sort()
# =========================================

nums = [5, 1, 8, 3]

nums.sort()

print(nums)

# Output:
# [1, 3, 5, 8]

# =========================================
# 11. reverse()
# =========================================

nums.reverse()

print(nums)

# Output:
# [8, 5, 3, 1]

# =========================================
# 12. count()
# =========================================

data = [1, 2, 1, 3, 1]

print(data.count(1))

# Output:
# 3

# =========================================
# 13. index()
# =========================================

print(data.index(3))

# Output:
# 3

# =========================================
# DICTIONARY METHODS
# =========================================

student = {
    "name": "Jannu",
    "age": 22
}

# =========================================
# 14. keys()
# =========================================

print(student.keys())

# Output:
# dict_keys(['name', 'age'])

# =========================================
# 15. values()
# =========================================

print(student.values())

# Output:
# dict_values(['Jannu', 22])

# =========================================
# 16. items()
# =========================================

print(student.items())

# Output:
# dict_items([('name', 'Jannu'), ('age', 22)])

# =========================================
# 17. get()
# =========================================

print(student.get("name"))

# Output:
# Jannu

# =========================================
# 18. update()
# =========================================

student.update({"city": "Lucknow"})

print(student)

# Output:
# {'name': 'Jannu', 'age': 22, 'city': 'Lucknow'}

# =========================================
# SET METHODS
# =========================================

s = {1, 2, 3}

# =========================================
# 19. add()
# =========================================

s.add(4)

print(s)

# =========================================
# 20. remove()
# =========================================

s.remove(2)

print(s)

# =========================================
# 21. union()
# =========================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# Output:
# {1, 2, 3, 4, 5}

# =========================================
# 22. intersection()
# =========================================

print(a.intersection(b))

# Output:
# {3}

