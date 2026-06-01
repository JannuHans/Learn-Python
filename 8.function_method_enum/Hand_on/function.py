
##PYTHON FUNCTIONS
# A function is a block of reusable code that performs a specific task.

# Instead of writing the same code again and again, we put it inside a function and call it whenever needed.


# =========================================
# 1. SIMPLE FUNCTION
# =========================================

def greet():
    print("Hello World")

greet()

# Output:
# Hello World


# =========================================
# 2. FUNCTION WITH PARAMETERS
# =========================================

def greet_user(name):
    print("Hello", name)

greet_user("Jannu")

# Output:
# Hello Jannu


# =========================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# =========================================

def add(a, b):
    print(a + b)

add(10, 20)

# Output:
# 30


# =========================================
# 4. RETURN STATEMENT
# =========================================

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# Output:
# 8


# =========================================
# 5. PRINT VS RETURN
# =========================================

def using_print(a, b):
    print(a + b)

def using_return(a, b):
    return a + b

using_print(10, 20)

result = using_return(10, 20)
print(result)

# Output:
# 30
# 30


# =========================================
# 6. DEFAULT PARAMETERS
# =========================================

def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Jannu")

# Output:
# Welcome Guest
# Welcome Jannu







# =========================================
# 10. LOCAL VARIABLE
# =========================================

def local_demo():
    x = 10
    print(x)

local_demo()

# Output:
# 10


# =========================================
# 11. GLOBAL VARIABLE
# =========================================

x = 100

def global_demo():
    print(x)

global_demo()

# Output:
# 100


# =========================================
# 12. LAMBDA FUNCTION
# =========================================

square = lambda x: x * x

print(square(5))

# Output:
# 25




# =========================================
# 14. BUILT-IN FUNCTIONS
# =========================================

numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Output:
# 3
# 30
# 10
# 60





