#2. WHILE LOOP
# A while loop runs:
# until condition becomes False.

#while condition:
    # code

#Example
i = 1
while i <= 5:
    print(i)
    i += 1

#Reverse Counting
i = 10

while i >= 1:
    print(i)
    i -= 1


#User Input Example
password = ""

while password != "admin":
    password = input("Enter password: ")

print("Access granted")