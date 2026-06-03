#Python Built in Functions
#Python provides many built-in functions that are available without importing any module. Here are some of the most commonly used ones:

#1. abs()
#The abs() function returns the absolute value of the specified number.

# x = abs(-7.25)
# print(x)

# x = abs(3+5j)
# print(x)

#2.all() Function
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.

# myList = [True,True,1]
# x=all(myList)
# print(x)

# dict = {0 : "Apple", 1 : "Orange"}
# x = all(dict)
# print(x)

# Returns False because the first key is false.For dictionaries the all() function checks the keys, not the values.

#3.any() Function
# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.

# mytuple = (0, 1, False)
# x = any(mytuple)
# print(x)

#4.bin() Function
# The bin() function returns the binary version of a specified integer.
# The result will always start with the prefix 0b.

# x=bin(7)
# print(x)

# 5.bool() Function
# The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None

# x = bool(1)
# print(x)

#6.chr() Function
# The chr() function returns the character that represents the specified unicode.

# x = chr(64)
# print(x)

#7.dict() Function
# The dict() function creates a dictionary.

# x = dict(name = "John", age = 36, country = "Norway")
# print(x)

#8.enumerate() Function
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)

# print(list(y))

#9.type() function
# The type() function returns the type of the specified object

# a = ('apple', 'banana', 'cherry')
# b = "Hello World"
# c = 33

# print(type(a))
# print(type(b))
# print(type(c))

#10.sum() function 
#The sum() function returns a number, the sum of all items in an iterable.

# a = (1, 2, 3, 4, 5)
# x = sum(a)
# print(x)

#11.str() function
#The str() function converts the specified value into a string.

# x = str(3.5)
# print(x)

# 12.slice() Function
# The slice() function returns a slice object.
# A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

# slice(start, end, step)

# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(0, 8, 3)
# print(a[x])

# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2)
# print(a[x])

# 13.sorted() function
# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically

# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)

# a = ("Jenifer", "Sally", "Jane")
# x = sorted(a, key=len)
# print(x)

# 14.round() 
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# The default number of decimals is 0, meaning that the function will return the nearest integer.

# x = round(5.76543, 2)
# print(x)

# x = round(5.76543)
# print(x)

# 15.pow()
# The pow() function returns the value of x to the power of y (xy).

# x = pow(4, 3)
# print(x)

# 16. id() 
# The id() function returns a unique id for the specified object.
    
# x = ('apple', 'banana', 'cherry')
# y = id(x)
# print(y)

#17.input()
# The input() function allows user input.

# print("Enter your name:")
# x = input()
# print("Hello, " + x)

# 18.len() function
#The len() function returns the number of items in an object.

# mylist = ["apple", "orange", "cherry"]
# x = len(mylist)
# print(x)

# 19.max() functio
# The max() function returns the item with the highest value, or the item with the highest value in an iterable.

# x = max(5, 10)
# print(x)

# 20. min()
# Return the lowest number:

# x = min(5, 10)
# print(x)
