#Basic Python Concepts

#Taking Input
#You can take input from the user using the input() function. By default, it returns the input as a string.
name = input("Enter your name: ")  # Takes input as string
print("Hello, " + name)

#Type Conversion of Input: If you want to store the input as an integer or float, convert it using int() or float().
age = int(input("Enter your age: "))  # Convert input to integer
print("Your age is", age)


#Comments in Python
#You can use comments to explain your code.
#Single-line Comment:
# This is a single-line comment
print("Hello, world!")  # This will print "Hello, world!"

#Multi-line Comment:
"""
This is a multi-line comment
You can explain a block of code
or give more details here
"""
print("Multi-line comments are useful for explanation.")


#Variables in Python
#Variables are used to store data. You don't need to declare a variable type in Python.
x = 10  # Integer
y = "Hello"  # String
z = 3.14  # Float

#Assigning multiple variables:
a, b, c = 5, "apple", 2.5  # Assign multiple variables in a single line


#Operators in Python
#Operators are used to perform operations on variables and values.
#Arithmetic Operators:
a = 5
b = 3
print(a + b)  # Addition: 8
print(a - b)  # Subtraction: 2
print(a * b)  # Multiplication: 15
print(a / b)  # Division: 1.666...
print(a % b)  # Modulus: 2 (remainder)
print(a ** b)  # Exponentiation: 125 (5^3)
print(a // b)  # Floor division: 1 (integer division)

#Comparison Operators:
x = 5
y = 10
print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True
print(x > y)   # Greater than: False
print(x < y)   # Less than: True
print(x >= y)  # Greater than or equal to: False
print(x <= y)  # Less than or equal to: True

#Logical Operators:
a = True
b = False
print(a and b)  # AND: False
print(a or b)   # OR: True
print(not a)    # NOT: False


#Type Casting (Type Conversion)
#You can convert one data type to another using type casting.
#Convert to Integer:
x = "10"  # String
y = int(x)  # Convert string to integer
print(type(y))  # <class 'int'>

#Convert to Float:
x = "3.14"  # String
y = float(x)  # Convert string to float
print(type(y))  # <class 'float'>

#Convert to String:
x = 123  # Integer
y = str(x)  # Convert integer to string
print(type(y))  # <class 'str'>

#Convert to Boolean:
x = 0  # Integer (False)
y = bool(x)  # Convert to Boolean
print(y)  # False


'''
Summary
Input allows user interaction.
Comments are used to explain code.
Variables store values (no need for type declaration).
Operators perform calculations or logical comparisons.
Type Casting converts one data type to another.
'''