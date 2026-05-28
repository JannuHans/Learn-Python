#Shallow Copy
# A shallow copy creates:

# New outer object
# But nested objects remain shared

import copy

list1 = [2,[1, 2], [3, 4]]

list2 = copy.copy(list1)

list2[1][0] = 100



print("Original:", list1)
print("Copied:", list2)

list2[0] = 100
print("Original:", list1)
print("Copied:", list2)



# 2.Deep Copy

# Deep copy creates:

# Completely independent copy
# Nested objects also copied separately



list1 = [[1, 2], [3, 4]]

list2 = copy.deepcopy(list1)

list2[0][0] = 100

print("Original:", list1)
print("Copied:", list2)