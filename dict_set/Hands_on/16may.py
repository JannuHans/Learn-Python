#               ****** DICTIONARY & SET (16 MAY) ******

# Dictionary (dict) stores key-value pairs.
# - Keys must be unique and immutable (e.g., str, int, tuple)
# - Values can be any type

student = {
    "name": "Jannu",
    "age": 22,
    "course": "Python",
    "skills": ["basics", "lists"],
}

print(student)
print(type(student))

# Access values
print(student["name"])      # bracket access (KeyError if key missing)
print(student.get("city")) # get() returns None if key missing
print(student.get("city", "Unknown"))

# Add / Update
student["city"] = "Jammu"          # add new key
student["age"] = 23                # update existing key
student.update({"course": "Core Python", "year": 2026})
print(student)

# Dictionary views
print(student.keys())
print(student.values())
print(student.items())

# Loop through a dict
for key in student:
    print(key, "->", student[key])

for key, value in student.items():
    print(f"{key} = {value}")

# Remove items
removed_age = student.pop("age")
print("removed age:", removed_age)

last_item = student.popitem()  # removes the last inserted item 
print("popitem:", last_item)

# Copy
student_copy = student.copy()
print("copy:", student_copy)

# Dictionary comprehension
squares = {n: n * n for n in range(1, 6)}
print("squares:", squares)


# -------------------- SET --------------------
# Set stores unique items (no duplicates). Unordered collection.

nums = {1, 2, 3, 3, 4, 4, 5}
print(nums)  # duplicates removed automatically

# Create empty set (IMPORTANT: {} is an empty dict)
empty_set = set()
print(type(empty_set))

# Add elements
nums.add(10)
nums.update([20, 30, 30])
print(nums)

# Remove elements
nums.remove(2)   # error if item not present
nums.discard(99) # no error if item not present
print(nums)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("union:", A | B)
print("intersection:", A & B)
print("difference A-B:", A - B)
print("difference B-A:", B - A)
print("symmetric difference:", A ^ B)

# Membership test
print(3 in A)
print(100 in A)
