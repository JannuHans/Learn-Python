# PYTHON OPERATORS NOTES


# 1. WHAT ARE OPERATORS?

# Operators are special symbols used to perform
# operations on variables and values.

a = 10
b = 5

print(a + b)   # Addition Output: 15


# TYPES OF OPERATORS IN PYTHON

# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators


# 1. ARITHMETIC OPERATORS

# Used for mathematical calculations.

# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# %   Modulus (Remainder)
# **  Exponent (Power)
# //  Floor Division

a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333
print(a % b)    # 1
print(a ** b)   # 1000
print(a // b)   # 3


# 2. ASSIGNMENT OPERATORS

# Used to assign values to variables.

# =    x = 5
# +=   x += 3   -> x = x + 3
# -=   x -= 3   -> x = x - 3
# *=   x *= 3   -> x = x * 3
# /=   x /= 3   -> x = x / 3
# %=   x %= 3   -> x = x % 3
# //=  x //= 3  -> x = x // 3
# **=  x **= 3  -> x = x ** 3

x = 10

x += 5
print(x)   # 15

x *= 2
print(x)   # 30

x -= 10
print(x)   # 20


# 3. COMPARISON OPERATORS

# Compare two values and return True or False.

# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to

a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False


# 4. LOGICAL OPERATORS

# Used to combine conditional statements.

# and
# or
# not

age = 20
has_id = True

print(age > 18 and has_id)   # True
print(age < 18 or has_id)    # True
print(not has_id)            # False


# 5. IDENTITY OPERATORS

# Used to compare memory locations of objects.

# is
# is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False

# == checks values
print(a == c)       # True

# is checks memory location


# 6. MEMBERSHIP OPERATORS

# Used to check whether a value exists
# inside a sequence.

# in
# not in

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)         # True
print("grapes" not in fruits)     # True


# 7. BITWISE OPERATORS

# Work on binary numbers (bits).

# &   AND
# |   OR
# ^   XOR
# ~   NOT
# <<  Left Shift
# >>  Right Shift

a = 5      # Binary: 0101
b = 3      # Binary: 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6


# OPERATOR PRECEDENCE

# Precedence decides which operation runs first.

print(2 + 3 * 4)

# Output:
# 14

# Explanation:
# 3 * 4 = 12
# 12 + 2 = 14

# Use brackets to change precedence.

print((2 + 3) * 4)

# Output:
# 20


# REAL-LIFE EXAMPLE

name = "Jannu"
age = 22
salary = 50000

if age >= 18 and salary > 30000:
    print(name, "is eligible")
else:
    print(name, "is not eligible")


# IMPORTANT DIFFERENCES

# Difference between = and ==

x = 5      # Assignment
print(x == 5)   # Comparison


# Difference between == and is

# == compares values
# is compares memory location

a = [1, 2]
b = [1, 2]

print(a == b)   # True
print(a is b)   # False


# PRACTICE QUESTIONS

# Q1
x = 10
x += 5
print(x)    # 15


# Q2
a = 5
b = 10

print(a > 2 and b < 20)   # True


# Q3
name = "Python"

print("P" in name)   # True
