# #Tuples are used to store multiple items in a single variable.


# #1. Tuple is Immutable
# #Once a tuple is created, its values cannot be changed, added, or removed.

# tuple1 = (1,2,4,2)

# tuple1[0]=6
# print(tuple1)

# #Why Tuple is Immutable?
# # Because tuples are designed for:fixed data,safer data handling

#coordinates = (49.67,45.67)

# # Coordinates should not accidentally change.

# # Tuples do not have methods like:
# # append()
# # remove()
# # pop()
# # insert()


#del tuple1

# # print(tuple1)

# # Mutable Object Inside Immutable Tuple
#data=([1,2],[5,6])

# data[0].append(3)
# print(data)

# # here Tuple references did not change.But internal list object changed.

# # data = ([1, 2], [3, 4])
# # data[0] = [10, 20]
# # TypeError

# #we are trying to change tuple reference.

# tuple2 = (1,2,3,4)
# print(id(tuple2))

# x = tuple2
# print(id(x))

# x = x+(6,)
# print(id(x))

# #Immutable vs Mutable Memory Behavior
# # a = [1,5,6]
# # b=a
# #a.append(3)
# # print(a)
# # print(b)

# a=(1,2,3)
# b=a

# a+=(4,)

# print(a)
# print(b)



# #2Ordered
# #Elements are stored in a fixed sequence/order.Python remembers: which element came first, second etc

# data = ("apple", "banana", "mango")

# print(data)
# # The order stays same.

# # index 0 → apple
# # index 1 → banana
# # index 2 → mango

# #we can access elements using index
# print(data[0])
# print(data[1])
# print(data[2])

# #3Indexing (positive + negative)
# #Index:    0         1         2         3
# #Tuple: ("apple", "banana", "mango", "orange")

# # Index:    -4       -3        -2        -1
# # Tuple: ("apple", "banana", "mango", "orange")

# # Useful when: you want last element, length is unknown

# data = (
#     ("Jannu", 21),
#     ("Hans", 22)
# )

# print(data[0])
# print(data[0][0])
# print(data[1][1])

# d = ("Python", "Java")

# print(d[0][0])

# #Slicing (Return new tuple)- Extracting a portion (part) of a tuple.

# #tuple[start : stop : step]
# numbers = (10, 20, 30, 40, 50)

# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[2:])
# print(numbers[::2])
# print(numbers[::-1])


# #Slicing Creates New Tuple
# a = (1, 2, 3, 4)

# b = a[1:3]

# print(b)
# print(id(a))
# print(id(b))


# #example
# data = (
#     ("a", "b", "c"),
#     (1, 2, 3, 4),
#     "Python"
# )

# print(data[0][1:])
# print(data[1][::-1])
# print(data[2][1:5])


# # Iterable- An object whose elements can be accessed one-by-one using a loop.

# data = (10, 20, 30)

# for x in data:
#     print(x)


# data = (10, 20, 30)
# i = 0
# while i < len(data):
#     print(data[i])
#     i += 1


# data = ("Python", "Java")

# for word in data:
#     for ch in word:
#         print(ch)

# #Concatenation
# a = (1, 2)
# b = (3, 4)

# c = a + b

# print(a)
# print(b)
# print(c)



# #Nested List in Tuple

# data = ([1, 2, 3], [4, 5])

# data[0].append(6)

# print(data)


# #Shallow Copy

# #Shallow copy creates:
# # NEW outer object
# # but inner objects are SHARED

# import copy

# data = ([1, 2], [3, 4])

# shallow = copy.copy(data)

# print(id(data[0]))
# print(id(shallow[0]))


# shallow[0].append(100)

# print(data)
# print(shallow)


# #Deep Copy
# # Deep copy creates:
# # NEW outer object
# # NEW inner objects also
# # Everything becomes independent.

# import copy

# data = ([1, 2], [3, 4])

# deep = copy.deepcopy(data)

# print(id(data[0]))
# print(id(deep[0]))

# deep[0].append(100)

# print(data)
# print(deep)



# x = data[:]

# x[0].append(100)

# print(data)
# print(x)

# #Tuple Multiplication
# data = (1, 2)
# print(data * 3)

# data = ([0] * 3,) * 3
# print(data)

# data[0][0] = 100
# print(data)

# #Tuple has only 2 built-in methods:

# # count()
# # index()
# t = (1, 2, 3, 2, 4, 2)

# print(t.count(2))
# print(t.index(2))
# print(t.index(2, 2))

# data = (1, True, 1)

# print(data.count(1))


# age = 18

# if age >= 18:
#     print("Eligible to vote")



# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# marks = 85

# if marks >= 90:
#     print("Grade A")

# elif marks >= 75:
#     print("Grade B")

# elif marks >= 50:
#     print("Grade C")

# else:
#     print("Fail")



# num = 10

# if num > 0:
    
#     if num % 2 == 0:
#         print("Positive Even")
    
#     else:
#         print("Positive Odd")

# else:
#     print("Negative")





# user = {
#     "name": "Jannu",
#     "age": 21,
#     "is_admin": True
# }

# if user:  

#     if user["age"] >= 18 and user["is_admin"]:
#         print("Admin access granted")

#     else:
#         print("Normal user")

# else:
#     print("No user data")

# two sum probles
