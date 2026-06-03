#Try, Except, else and Finally in Python
#Exception handling is used to handle errors gracefully so that the program does not crash.

# Try: This block will test the excepted error to occur
# Except:  Here you can handle the error
# Else: If there is no exception then this block will be executed
# Finally: Finally block always gets executed either exception is generated or not



# try:
#        # Some Code.... 
# except:
#        # optional block
#        # Handling of exception (if required)
# else:
#        # execute if no exception
# finally:
#       # Some code .....(always executed)



#           try
#            |
#     ----------------
#     |              |
#  No Error       Error
#     |              |
#    else         except
#     \              /
#      \            /
#        finally
#           |
#         End



# #1. ValueError
# # Occurs when the value is invalid, even though the data type is correct.

# try:
#     num = int("abc")
# except ValueError as e:
#     print(e)

# # 2. TypeError
# # Occurs when an operation is performed on an unsupported data type.

# try:
#     print("10" + 5)
# except TypeError as e:
#     print(e)

# 3. ZeroDivisionError
# Occurs when dividing by zero.

# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)

# 4. IndexError
# Occurs when accessing a list index that doesn't exist.

# try:
#     numbers = [1, 2, 3]
#     print(numbers[5])
# except IndexError as e:
#     print(e)

# 5. KeyError
# Occurs when accessing a dictionary key that doesn't exist.

# try:
#     student = {"name": "Kavir"}
#     print(student["age"])
# except KeyError as e:
#     print(e)

# 6. AttributeError
# Occurs when an object doesn't have the attribute or method you're trying to use.

# try:
#     name = "Python"
#     name.append("A")
# except AttributeError as e:
#     print(e)

#def divide(x, y): 
#     try: 
#         result = x // y 
#         print("Yeah ! Your answer is :", result) 
#     except ZeroDivisionError: 
#         print("Sorry ! You are dividing by zero ") 
  
# divide(3, 2) 
# divide(3, 0)



# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     print(result)
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"An error occurred: {e}")


 
# def divide(x, y): 
#     try: 
       
#         result = x // y 
#     except ZeroDivisionError: 
#         print("Sorry ! You are dividing by zero ") 
#     else:
#         print("Yeah ! Your answer is :", result) 
  

# divide(3, 2) 
# divide(3, 0)



# def divide(x, y): 
#     try: 
        
#         result = x // y 
#     except ZeroDivisionError: 
#         print("Sorry ! You are dividing by zero ") 
#     else:
#         print("Yeah ! Your answer is :", result) 
#     finally:  
       
#         print('This is always executed')   


# divide(3, 2) 
# divide(3, 0)


class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw = 2000

try:
    if withdraw > balance:
        raise InsufficientBalanceError(
            "Not enough balance in account"
        )

except InsufficientBalanceError as e:
    print(e)
else:
    print("ok ok") 