#A set is a collection of unique color names that are unordered and unindexed. Sets are written using curly brackets {}.
#Unordered: Items have no index.
#No duplicate items: A set does not allow duplicate color names.
#Mutable: You can add or remove items.

#Creating a Set of Color Names:
colors = {"red", "blue", "green"}
print(colors)  # {'red', 'blue', 'green'}

#Creating an Empty Set:
empty_set = set()  # Use the set() function to create an empty set
print(empty_set)  # set()


#Accessing Items in a Set
#Since sets are unordered, you cannot access items by index. However, you can loop through a set to access its color names.
#Looping Through a Set:
colors = {"red", "blue", "green"}
for color in colors:
    print(color)

#Check if a Color is in a Set:
colors = {"red", "blue", "green"}
print("blue" in colors)  # True
print("yellow" in colors)  # False


#Adding Colors to a Set
#You can add single or multiple color names to a set using the add() and update() methods.
#Adding a Single Color:
colors.add("yellow")
print(colors)  # {'red', 'blue', 'green', 'yellow'}

#Adding Multiple Colors:
colors.update(["purple", "orange"])
print(colors)  # {'red', 'blue', 'green', 'yellow', 'purple', 'orange'}


#Removing Colors from a Set
#You can remove color names from a set using the remove(), discard(), or pop() methods.
#Using remove():
colors.remove("green")
print(colors)  # {'red', 'blue', 'yellow', 'purple', 'orange'}
#Note: If the item does not exist, remove() raises an error.

#Using discard():
colors.discard("green")  # Does nothing if 'green' is not found
print(colors)  # {'red', 'blue', 'yellow', 'purple', 'orange'}

#Using pop():
color = colors.pop()  # Removes and returns an arbitrary color
print(color)  # Could be any color from the set
print(colors)  # Remaining colors in the set
 
#Using clear():
colors.clear()  # Removes all colors from the set
print(colors)  # set()


#Set Operations
#Union (| or union())
#The union of two sets returns a new set with all colors from both sets (duplicates are removed).
set1 = {"red", "blue", "green"}
set2 = {"yellow", "purple", "blue"}
set3 = set1.union(set2)  # Or use set1 | set2
print(set3)  # {'red', 'blue', 'green', 'yellow', 'purple'}

#Intersection (& or intersection())
#The intersection of two sets returns a new set with colors that are present in both sets.
set1 = {"red", "blue", "green"}
set2 = {"yellow", "blue", "orange"}
set3 = set1.intersection(set2)  # Or use set1 & set2
print(set3)  # {'blue'}

#Difference (- or difference())
#The difference of two sets returns a new set with colors that are only in the first set, but not in the second.
set1 = {"red", "blue", "green"}
set2 = {"yellow", "blue", "orange"}
set3 = set1.difference(set2)  # Or use set1 - set2
print(set3)  # {'red', 'green'}

#Symmetric Difference (^ or symmetric_difference())
#The symmetric difference of two sets returns a new set with colors that are in one set or the other, but not in both.
set1 = {"red", "blue", "green"}
set2 = {"yellow", "blue", "orange"}
set3 = set1.symmetric_difference(set2)  # Or use set1 ^ set2
print(set3)  # {'red', 'green', 'yellow', 'orange'}