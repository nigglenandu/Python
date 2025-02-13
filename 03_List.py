# List
# store multiple items in a single variable.
# ordered, changeable, and allow duplicate values.

#Creating a List
mylist = ["red", "blue", "green"]
print(mylist)  # ['red', 'blue', 'green']
print(len(mylist))  # 3
print(type(mylist))  # <class 'list'>


#Accessing List Items
print(mylist[1])  # 'blue'  (Access by index)
print(mylist[-1])  # 'green' (Negative indexing)
print(mylist[1:3])  # ['blue', 'green'] (Slicing)


#Modifying List Items
mylist[1:2] = ["yellow", "pink"]  # Replace 'blue' with 'yellow', 'pink'
print(mylist)  # ['red', 'yellow', 'pink', 'green']

mylist[1] = "orange"  # Change 'yellow' to 'orange'
print(mylist)  # ['red', 'orange', 'pink', 'green']

mylist.insert(2, "purple")  # Insert 'purple' at index 2
print(mylist)  # ['red', 'orange', 'purple', 'pink', 'green']

mylist.append("black")  # Add 'black' at the end
print(mylist)  # ['red', 'orange', 'purple', 'pink', 'green', 'black']


#Merging Lists
thislist = list(("white", "brown"))  # Creating a list using list()
mylist.extend(thislist)  # Merge lists
print(mylist)  # ['red', 'orange', 'purple', 'pink', 'green', 'black', 'white', 'brown']


#Removing Items from a List
mylist.remove("purple")  # Remove 'purple'
print(mylist)  # ['red', 'orange', 'pink', 'green', 'black', 'white', 'brown']

mylist.pop(1)  # Remove item at index 1 ('orange')
print(mylist)  # ['red', 'pink', 'green', 'black', 'white', 'brown']

del mylist[1]  # Delete item at index 1 ('pink')
print(mylist)  # ['red', 'green', 'black', 'white', 'brown']

# mylist.clear()  # Removes all elements from the list


#Looping Through a List
for x in mylist:
    print(x)

#Using List Comprehension
[print(x) for x in mylist]

#Using a While Loop
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1


#List Comprehension (Filtering & Transforming)
# New list with elements that contain 'r'
mylist = [x for x in mylist if "r" in x]
print(mylist)  # ['red', 'green', 'brown']


#Creating a List from a Range
newlist = [x for x in range(4)]
print(newlist)  # [0, 1, 2, 3]


#Transforming a List
mylist = [x.upper() for x in mylist]  # Convert all items to uppercase
print(mylist)

mylist.sort()  # Sort list in ascending order
print(mylist)

mylist.sort(reverse=True)  # Sort in descending order
print(mylist)

mylist.reverse()  # Reverse the order of the list
print(mylist)


#Copying a List
mylist = newlist.copy()  
print(mylist)

mylist = list(newlist)  
print(mylist)

mylist = newlist[:]  
print(mylist)


#Joining Two Lists
anotherList = mylist + newlist
print(anotherList)