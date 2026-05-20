#                       ****Python Data Types***

#A data type tells Python what kind of value a variable is storing.

# 1. Integer (int)
# Integers are whole numbers without decimal points

from numpy import nan


age = 22
print(age)
print(type(age))

# Output:
# 22
# <class 'int'>

# 2. Float (float)
# Float means numbers with decimal values.

price = 64.40
print(price)
print(type(price))

# Output:
# 64.4
# <class 'float'>

value = 15/5
print(value)
print(type(value))

# Output:
# 3.0   
# <class 'float'>


# 3. String (str):
#This is used to store anything in python, literally anything that are available on your keyboard.
# You have to use quotes to store anything and it will be considered as string. You can use double
# Quotes (“”) or single quotes (‘’) to store both works same.

name = "Jannu"
print(name)
print(type(name))
# output:
# Jannu
# <class 'str'>

Lname = 'Hans'
print(Lname)
print(type(Lname))
# output:
# Hans  
# <class 'str'>

# String Slicing
print(name[0:3])  # Output: Jan
print(name[1:4])  # Output: ann 

Full_name = name + " " + Lname
print(Full_name)  # Output: Jannu Hans  

print(name.upper() )  # Output: JANNU
print(Full_name[0:6:2]) # Output: Jnu


# 4. Boolean (bool):
# Boolean stores only:True or False. Used in conditions and decision making.

is_adult = True
print(is_adult)
print(type(is_adult))

# Output:
# True
# <class 'bool'>

a = 14
b = 18
c=a>b
print(c)    
print(type(c))

# Output:
# False
# <class 'bool'>

# 5. List (list):
# A list is a collection of items in a particular order. Lists are mutable, meaning you can change their content after creation. Lists are defined using square brackets [].

my_list = [1, 2, 3, 4]
print(my_list)
print(type(my_list))

# Output:
# [1, 2, 3, 4]  
# <class 'list'>

Fruits = ["apple", "banana", "mango"]

# Creating a list of integers
numbers = [10, 20, 30, 40]

# Lists can even hold different data types
mixed_list = [1, "Hello", 3.14, True]

#Indexing
print(Fruits[0])  # Output: apple
print(numbers[1])  # Output: 20

# Modifying a list
Fruits[1] = "orange"    
print(Fruits)  # Output: ['apple', 'orange', 'mango']

#Basic List Methods :
# .append() - Adds an item to the end of the list.
# .insert() - Inserts an item at a specified position.    
# .remove() - Removes the first occurrence of a specified item.
# .pop() - Removes and returns an item at a specified position (default is the last item).

numbers.append(50)
print(numbers)  # Output: [10, 20, 30, 40, 50]  
numbers.insert(2, 25)
print(numbers)  # Output: [10, 20, 25, 30, 40, 50]



# 6. Tuple:
# A tuple is similar to a list but is immutable, meaning you cannot change its content after creation. Tuples are defined using parentheses ().
my_tuple = (1, 2, 3, 4)
print(my_tuple) 
print(type(my_tuple))
# Output:
# (1, 2, 3, 4)
# <class 'tuple'>

print(my_tuple[0])  # Output: 1

# 7. Dictionary (dict):
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are defined using curly braces {}.

my_dict = {"name": "jannu", "age": 22, "city": "Jammu"}
print(my_dict)  
print(type(my_dict))
# Output:
# {'name': 'jannu', 'age': 22, 'city': 'Jammu'}
# <class 'dict'>


# 7. Set:
# A set is an unordered collection of unique items. Sets are defined using curly braces {} or the set() function.

my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))
# Output:
# {1, 2, 3, 4}
# <class 'set'>

