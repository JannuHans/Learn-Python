# #1. Local Variable
# # A variable declared inside a function is called a local variable.

# # It exists only inside the function.
# # Cannot be accessed outside the function.

# def student():
#     name = "Jannu"   # Local Variable
#     print(name)

# student()




# # def student():
# #     name = "Jannu"

# # student()

# # print(name)   #  Error


# # 2. Global Variable
# # A variable declared outside the function is called a global variable.

# # Can be accessed anywhere in the program.



# college = "IET Lucknow"   # Global Variable

# def show():
#     print(college)

# show()
# print(college)


# # 3. Global Keyword
# # If you want to modify a global variable inside a function, use global.
# count = 10

# def update():
#     global count
#     count = 50

# update()

# print(count)




# x = 100

# def test():
#     x = 50
#     print(x)

# test()
# print(x)





