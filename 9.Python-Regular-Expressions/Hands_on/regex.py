"""
====================================================
PYTHON REGULAR EXPRESSIONS (REGEX) - NOTES + HANDS ON
Source: W3Schools Python Regex
====================================================

WHAT IS REGEX?
--------------
Regex (Regular Expression) is a sequence of characters
that forms a search pattern.

It is used for:
1. Searching text
2. Matching patterns
3. Replacing text
4. Validating data

Python provides the 're' module for regex operations.

----------------------------------------------------
IMPORT REGEX MODULE
----------------------------------------------------
"""

import re

# ==================================================
# 1. re.search()
# ==================================================
# Searches the string for a match.
# Returns a Match object if found, otherwise None.

txt = "The rain in Spain"

result = re.search("Spain", txt)

print("Search Example:")
print(result)
print()


# ==================================================
# 2. re.findall()
# ==================================================
# Returns a list containing all matches.

txt = "The rain in Spain"

result = re.findall("ai", txt)

print("Findall Example:")
print(result)
print()

# If no match found:
result = re.findall("India", txt)
print(result)
print()


# ==================================================
# 3. re.split()
# ==================================================
# Splits the string at each match.

txt = "The rain in Spain"

result = re.split(r"\s", txt)

print("Split Example:")
print(result)
print()

# Split only at first occurrence
result = re.split(r"\s", txt, 1)

print(result)
print()


# ==================================================
# 4. re.sub()
# ==================================================
# Replaces matches with another string.

txt = "The rain in Spain"

result = re.sub(r"\s", "-", txt)

print("Sub Example:")
print(result)
print()

# Replace first 2 spaces only
result = re.sub(r"\s", "-", txt, 2)

print(result)
print()


# ==================================================
# MATCH OBJECT
# ==================================================
# Returned by search() if a match exists.

txt = "The rain in Spain"

match = re.search("Spain", txt)

print("Match Object:")
print(match)
print()


# ==================================================
# .span()
# ==================================================
# Returns start and end position.

match = re.search(r"\bS\w+", txt)

print("Span:")
print(match.span())
print()


# ==================================================
# .string
# ==================================================
# Returns original string.

print("String:")
print(match.string)
print()


# ==================================================
# .group()
# ==================================================
# Returns matched text.

print("Group:")
print(match.group())
print()


# ==================================================
# REGEX METACHARACTERS
# ==================================================

"""
[]   Set of characters
\    Special sequence
.    Any character except newline
^    Starts with
$    Ends with
*    Zero or more occurrences
+    One or more occurrences
?    Zero or one occurrence
{}   Exact number of occurrences
|    Either OR
()   Group
"""


# ==================================================
# SPECIAL SEQUENCES
# ==================================================

txt = "My number is 123"

# \d = digit
print(re.findall(r"\d", txt))
print()

# \D = non-digit
print(re.findall(r"\D", txt))
print()

# \s = whitespace
print(re.findall(r"\s", txt))
print()

# \S = non-whitespace
print(re.findall(r"\S", txt))
print()

# \w = letters, digits, underscore
print(re.findall(r"\w", txt))
print()

# \W = not word characters
print(re.findall(r"\W", txt))
print()


# ==================================================
# SETS []
# ==================================================

txt = "hello 123"

# Find any character between a and h
print(re.findall(r"[a-h]", txt))

# Find digits
print(re.findall(r"[0-9]", txt))

# Find letters
print(re.findall(r"[a-z]", txt))

print()


# ==================================================
# PRACTICAL EXAMPLES
# ==================================================

# Example 1: Check if string starts with "The"

txt = "The rain in Spain"

if re.search(r"^The", txt):
    print("Starts with The")
else:
    print("No match")

print()


# Example 2: Check if string ends with "Spain"

if re.search(r"Spain$", txt):
    print("Ends with Spain")
else:
    print("No match")

print()


# Example 3: Extract all numbers

txt = "Order 123, Product 456, Bill 789"

numbers = re.findall(r"\d+", txt)

print("Numbers:")
print(numbers)
print()


# Example 4: Extract email

txt = "Contact us at support@gmail.com"

email = re.findall(r"\S+@\S+", txt)

print("Email:")
print(email)
print()


# Example 5: Replace digits

txt = "My phone number is 9876543210"

result = re.sub(r"\d", "*", txt)

print(result)
print()


# ==================================================
# HANDS-ON PRACTICE QUESTIONS
# ==================================================

"""
Q1. Find all digits from:
    "abc123xyz456"

Q2. Find all spaces from:
    "Python is fun"

Q3. Extract all words from:
    "Hello! My name is Jannu."

Q4. Check whether string starts with "Hello"

Q5. Check whether string ends with "India"

Q6. Replace all spaces with "_"

Q7. Split:
    "apple,banana,mango"

using comma.

Q8. Extract all email IDs from:
    "abc@gmail.com xyz@yahoo.com"

Q9. Find all numbers from:
    "Price: 500, Discount: 20"

Q10. Replace all digits with X.
"""


# ==================================================
# HANDS-ON SOLUTIONS
# ==================================================

# Q1
print(re.findall(r"\d+", "abc123xyz456"))

# Q2
print(re.findall(r"\s", "Python is fun"))

# Q3
print(re.findall(r"\w+", "Hello! My name is Jannu."))

# Q4
print(bool(re.search(r"^Hello", "Hello World")))

# Q5
print(bool(re.search(r"India$", "I love India")))

# Q6
print(re.sub(r"\s", "_", "Python is fun"))

# Q7
print(re.split(",", "apple,banana,mango"))

# Q8
print(re.findall(r"\S+@\S+", "abc@gmail.com xyz@yahoo.com"))

# Q9
print(re.findall(r"\d+", "Price: 500, Discount: 20"))

# Q10
print(re.sub(r"\d", "X", "My number is 12345"))


# ==================================================
# MOST IMPORTANT REGEX PATTERNS 
# ==================================================

"""
\d      Digit (0-9)
\D      Non-digit
\s      Whitespace
\S      Non-whitespace
\w      Word character
\W      Non-word character

^       Start of string
$       End of string

+       One or more
*       Zero or more
?       Optional

[a-z]   Lowercase letters
[A-Z]   Uppercase letters
[0-9]   Digits

\b      Word boundary

\d+     One or more digits
\w+     One or more word characters

^Hello  Starts with Hello
India$  Ends with India
"""

print("\nRegex Notes Completed!")