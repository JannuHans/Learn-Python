#             ******LIST, TUPLE, DICTIONARY******

# 1. List: A list is a collection of items that are ordered and changeable. It is defined using square brackets [].

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(type(mylist))
# Output:
# <class 'list'>    

#Access Items
#List items are indexed and you can access them by referring to the index number

print(mylist[0])  # Output: apple
print(mylist[-1])  # Output: mango
print(mylist[2:5])  # Output: ['cherry', 'orange', 'kiwi']

if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Output:
# ['apple', 'blackcurrant', 'cherry']

#Insert Items:
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# Output:
# ['apple', 'banana', 'watermelon', 'cherry']

#Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   
print(thislist)
# Output:   
# ['apple', 'banana', 'cherry', 'orange']

#Extend List
#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Output:
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Remove Specified Item

#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# Output:
# ['apple', 'cherry']

#The pop() method removes the specified index.If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# Output:
# ['apple', 'cherry']   

#The del keyword also removes the specified index:The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist[0] 
print(thislist)     
# Output:
# ['banana', 'cherry']  
del thislist
# print(thislist)  # This will raise an error because the list has been deleted.

#The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# Output:
# []