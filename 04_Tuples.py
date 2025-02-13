# A tuple is used to store multiple items in a single variable.
# Ordered, Unchangeable (Immutable), Allows duplicate values, Defined using parentheses ()

#Creating a Tuple
mytuple = ("red", "blue", "green")
print(mytuple)  # ('red', 'blue', 'green')

#Tuple with One Item: Add a comma after the element; otherwise, it will not be recognized as a tuple.
one_item_tuple = ("red",)  
print(type(one_item_tuple))  # <class 'tuple'>

not_a_tuple = ("red")  
print(type(not_a_tuple))  # <class 'str'> (NOT a tuple!)

#Using tuple() Constructor:
mytuple = tuple(("red", "blue", "green"))  # Using the tuple() function
print(mytuple)

#Accessing Tuple Items
print(mytuple[1])  # 'blue'  (Access by index)
print(mytuple[-1])  # 'green' (Negative indexing starts from the end)
print(mytuple[1:3])  # ('blue', 'green') (Slicing)

#Changing Tuple Values
#Tuples are immutable, meaning items cannot be changed directly.
#However, we can convert a tuple to a list, modify it, and convert it back.
x = ("red", "blue", "green")
y = list(x)  # Convert tuple to list
y[1] = "yellow"
x = tuple(y)  # Convert back to tuple
print(x)  # ('red', 'yellow', 'green')


#Adding and Removing Items
#Since tuples are immutable, we can't directly add or remove items. But we can workaround:
#Adding Items
mytuple += ("orange",)  # Concatenation (Creates a new tuple)
print(mytuple)  

#R#emoving Items
y = list(mytuple)
y.remove("blue")
mytuple = tuple(y)
print(mytuple)  # ('red', 'green', 'orange')

#Looping Through a Tuple
#Using for Loop
for item in mytuple:
    print(item)

#Using while Loop
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i += 1

#Tuple Methods
#Method	Description
#count(value)	Returns the number of times a value appears in the tuple
#index(value)	Returns the index of the first occurrence of a value
mytuple = ("red", "blue", "green", "blue")
print(mytuple.count("blue"))  # 2
print(mytuple.index("green"))  # 2

#Joining Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # ('a', 'b', 'c', 1, 2, 3)

#Tuple Packing & Unpacking
#Packing a Tuple
colors = ("red", "blue", "green")  # Packing multiple values into a tuple

#Unpacking a Tuple
(a, b, c) = colors
print(a)  # 'red'
print(b)  # 'blue'
print(c)  # 'green'

#Using * (Asterisk) for Remaining Values
colors = ("red", "blue", "green", "orange", "yellow")
(a, b, *c) = colors
print(a)  # 'red'
print(b)  # 'blue'
print(c)  # ['green', 'orange', 'yellow']

#Advantages of Tuples Over Lists
#✅ Faster than lists (better performance).
#✅ Immutable (data cannot be modified, which prevents accidental changes).
#✅ Can be used as dictionary keys (lists cannot).

#Tuple vs List (Key Differences)
#Feature	Tuple	List
#Mutable	❌ No	✅ Yes
#Performance	✅ Faster	❌ Slower
#Syntax	()	[]
#Can be Dictionary Keys	✅ Yes	❌ No
#Methods Available	count(), index()	Many (append(), remove(), etc.)
