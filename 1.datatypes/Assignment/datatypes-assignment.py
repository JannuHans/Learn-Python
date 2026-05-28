#1 Difference b/w float and decimal
#1. Float in Python
# float uses binary floating-point representation, so sometimes it gives small precision errors.

a = 0.1
b = 0.2

print(a + b)

# Output:
# 0.30000000000000004

#2. Decimal in Python
#Decimal stores numbers more accurately.
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)
# Output:
# 0.3

# Use float when:
# Speed is important
# Scientific calculations
# Graphics/game development
# Machine learning


# Use Decimal when:
# Money calculations
# Banking systems
# Financial reports
# High precision needed

# The biggest difference between float and Decimal in Python is: Precision (Accuracy)

#2. none == None
#  is a special constant in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything.
print(None == None)  # Output: True
print(None == 0)     # Output: False

# None is a special keyword in Python that represents:
# no value
# empty value
# absence of data
# It is an object of type NoneType.

# Python creates only one None object in memory.
# So:
# left None → same object, right None → same object
# Hence they are equal.


# . How we store string in python?
# Strings are Objects Stored in Memory.
# When you write

name = "Python"

# Python does these steps internally:
# Creates a string object "Python" in memory
# Stores characters one by one
# Variable name stores the reference/address of that object

#Python stores strings using Unicode. Each character is represented by a unique code point. For example:
# 'P' → U+0050      
# 'y' → U+0079
# 't' → U+0074

# Python sometimes reuses same strings to save memory.
#  a = "hello"
#  b = "hello"

# Both may point to the same memory object.
# a ---> "hello" <--- b
# This optimization is called: string interning. It helps save memory for commonly used strings.


#3.DocStrings in Python
# A DocString (Documentation String) is a special string used to describe:
# functions
# classes
# modules
# It helps programmers understand what the code does.
# DocStrings are written using triple quotes:
# """ """

def add(a, b):
    """This function returns the sum of two numbers"""
    return a + b

print(add(2, 3))

# Output:
# 5 

# Accessing DocString
# Use __doc__
print(add.__doc__)
# Output:
# This function returns the sum of two numbers

#A DocString is a special multi-line string used to document Python code.