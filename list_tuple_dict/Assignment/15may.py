#Part 1 — List Operations


## Create initial list
import numbers


my_list = [1, 33, 56, 1001, 768]
print(my_list) 

# 1. Add 89 to the end of the list
my_list.append(89)
print

# 2. Add 39 to the beginning of the list
my_list.insert(0, 39)
print(my_list)

# 3. Add elements of another list [77,66,44] into the existing list
list2 = [77, 66, 44]
my_list.extend(list2)
print(my_list)

# 4. Add [99,88] as a single nested element inside the list
my_list.append([99, 88])
print(my_list)

# 5. Insert 'Apple' at position 2
my_list.insert(2, 'Apple')
print(my_list)

# 6. Replace 'Apple' with 'Pineapple'
my_list[2] ='Pineapple'
print(my_list)

# 7. Remove the element present at position 4
my_list.pop(4)
print(my_list)

# 8. Remove 'Pineapple' from the list
my_list.remove('Pineapple')
print(my_list)


#Part 2 — Pair Sum Problem

# Given:
# list = [1,2,3,4,5,6,7,8]
# z = 9
# Find all pairs of elements whose sum is equal to z.

list = [1, 2, 3, 4, 5, 6, 7, 8]
z = 9
n = len(list)
temp = []

for i in range(n):
    for j in range(i + 1, n):
        if list[i] + list[j] == z:
            temp.append((list[i], list[j]))


result = tuple(temp)

print(result)