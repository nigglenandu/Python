'''Dictionary is an unordered collection of key-value pairs. Each key is unique and associated with a value, which can be any data type (e.g., string, number, list).
Unordered: Items have no index.
Key-Value Pairs: Each item is a pair where one value is the key, and the other is its corresponding value.
Mutable: You can change, add, or remove key-value pairs.
Creating a Dictionary of Color Names
'''

colors = {"red": "#FF0000", "blue": "#0000FF", "green": "#00FF00"}
print(colors)  # {'red': '#FF0000', 'blue': '#0000FF', 'green': '#00FF00'}

#Empty Dictionary:
empty_dict = {}
print(empty_dict)  # {}


#Accessing Dictionary Items
#You can access dictionary values by using their keys.
#Accessing a Value:
colors = {"red": "#FF0000", "blue": "#0000FF", "green": "#00FF00"}
print(colors["blue"])  # '#0000FF'

#Using get() Method:
print(colors.get("green"))  # '#00FF00'


#Modifying a Dictionary
#You can change the value associated with a key or add a new key-value pair.
#Changing the Value of a Key:
colors["blue"] = "#00008B"  # Change 'blue' color code
print(colors)  # {'red': '#FF0000', 'blue': '#00008B', 'green': '#00FF00'}

#Adding a New Key-Value Pair:
colors["yellow"] = "#FFFF00"
print(colors)  # {'red': '#FF0000', 'blue': '#00008B', 'green': '#00FF00', 'yellow': '#FFFF00'}


#Removing Items from a Dictionary
#You can remove items from a dictionary using several methods.
#Using pop() Method:
colors.pop("green")  # Removes the key 'green' and its value
print(colors)  # {'red': '#FF0000', 'blue': '#00008B', 'yellow': '#FFFF00'}

#Using del Keyword:
del colors["yellow"]  # Deletes the 'yellow' key-value pair
print(colors)  # {'red': '#FF0000', 'blue': '#00008B'}

#Using clear() Method:
colors.clear()  # Removes all items in the dictionary
print(colors)  # {}


#Looping Through a Dictionary
#You can loop through a dictionary to access its keys and values.
#Looping Through Keys:
for color in colors:
    print(color)  # Prints the key (e.g., 'red', 'blue')

#Looping Through Keys and Values:
for color, code in colors.items():
    print(color, code)  # Prints both key and value (e.g., 'red' '#FF0000')


#Dictionary Methods
#keys() Method: Returns a view object that displays all the keys in the dictionary.
print(colors.keys())  # dict_keys(['red', 'blue'])

#values() Method: Returns a view object that displays all the values in the dictionary.
print(colors.values())  # dict_values(['#FF0000', '#00008B'])

#items() Method: Returns a view object that displays a list of dictionary's key-value tuple pairs.
print(colors.items())  # dict_items([('red', '#FF0000'), ('blue', '#00008B')])


#Nested Dictionarie
#A dictionary can also contain other dictionaries as values, which is known as a nested dictionary.
#Example of a Nested Dictionary:
colors = {
    "red": {"rgb": "255, 0, 0", "hex": "#FF0000"},
    "blue": {"rgb": "0, 0, 255", "hex": "#0000FF"}
}
print(colors["red"]["hex"])  # '#FF0000'


#Using get() with Default Value
#If the key does not exist, the get() method allows you to provide a default value.
#Using get() with a Default Value:
print(colors.get("yellow", "Not Found"))  # 'Not Found'


#Copying a Dictionary
#You can create a copy of a dictionary.
#Copying Using copy() Method:
colors_copy = colors.copy()
print(colors_copy)  # {'red': '#FF0000', 'blue': '#00008B'}


#Joining Dictionaries
#You can merge dictionaries using the update() method.
#Merging Dictionaries:
new_colors = {"green": "#00FF00", "yellow": "#FFFF00"}
colors.update(new_colors)  # Merges new_colors into colors
print(colors)  # {'red': '#FF0000', 'blue': '#00008B', 'green': '#00FF00', 'yellow': '#FFFF00'}