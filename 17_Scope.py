'''
Scope refers to the region of the program where a variable is recognized. In Python, there are four types of scopes:

Local Scope: Variables defined inside a function or block.
Enclosing Scope: A scope that contains the local scope (used in nested functions).
Global Scope: Variables defined at the top level of a module or script.
Built-in Scope: The scope of built-in functions and exceptions.
'''

#Local and Global Scope
x = "global x"  # Global variable

def my_function():
    x = "local x"  # Local variable
    print("Inside function:", x)

my_function()
print("Outside function:", x)
#In this example, the x inside the function is local to the function and does not affect the global x.


#The global Keyword
#To modify a global variable inside a function, you need to use the global keyword:
x = "global x"

def my_function():
    global x
    x = "modified global x"

my_function()
print(x)  # Output: modified global x


#The nonlocal Keyword
#The nonlocal keyword is used to modify a variable in the nearest enclosing scope (excluding global scope).
def outer_function():
    x = "outer x"
    
    def inner_function():
        nonlocal x
        x = "modified outer x"
    
    inner_function()
    print(x)  # Output: modified outer x

outer_function()

'''
Scope Resolution (LEGB Rule)
Python follows the LEGB rule (Local, Enclosing, Global, Built-in) to resolve variable names:

Local: The innermost scope, which is the function where the variable is defined.
Enclosing: The scope of any enclosing functions.
Global: The top-level scope of the script or module.
Built-in: The outermost scope, which includes Python’s built-in names.
'''

#Scope Resolution
x = "global x"

def outer_function():
    x = "enclosing x"
    
    def inner_function():
        x = "local x"
        print(x)  # Output: local x
    
    inner_function()

outer_function()

#In this example, the inner_function prints the local variable x, which shadows the enclosing and global variables.

