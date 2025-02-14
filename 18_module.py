#A module is a file containing Python code (functions, variables, etc.) that can be imported into other scripts.

#Creating a Module
#Create a module by saving Python code in a .py file.

# mymodule.py
def greet(name):
    return f"Hello, {name}!"


#Using a Module
#Use import to include a module in your script.
import mymodule
print(mymodule.greet("Alice"))  # Output: Hello, Alice!


#Importing Specific Functions
#You can import specific functions from a module.
from mymodule import greet
print(greet("Bob"))  # Output: Hello, Bob!


#Aliasing a Module
#Assign an alias to a module for easier reference.
import mymodule as mm
print(mm.greet("Charlie"))  # Output: Hello, Charlie!


#The dir() Function
#Use dir() to list all functions and variables in a module.
import mymodule
print(dir(mymodule))  # Shows all functions and variables in mymodule


#The __name__ Variable
#Check if a module is being run directly or imported.
if __name__ == "__main__":
    print("This module is being run directly")
else:
    print("This module is being imported")


#Built-in Modules
#Use Python’s built-in modules like math for various functions.
import math
print(math.sqrt(16))  # Output: 4.0


#Installing External Modules
#Install third-party modules using pip.
#bash
#pip install requests

import requests
response = requests.get("https://www.example.com")
print(response.status_code)