#Creating a Function
#A function is defined using the def keyword.

def print_colors():
    print("red, blue, green")

print_colors()  # Calling the function


#Function with Parameters
#We can pass values (parameters) to a function.
def favorite_color(color):
    print("My favorite color is", color)

favorite_color("yellow")


#Function with Multiple Parameters
#We can pass multiple arguments.
def mix_colors(color1, color2):
    print("Mixing", color1, "and", color2)

mix_colors("red", "blue")


#Default Parameter Value
#If no argument is given, the default value is used.
def default_color(color="black"):
    print("The default color is", color)

default_color()  # No argument
default_color("white")  # Argument given


#Return Values
#A function can return a value.
def get_color():
    return "purple"

fav = get_color()
print(fav)


#Using *args (Multiple Arguments)
#Use *args to pass multiple values.
def print_all_colors(*colors):
    for color in colors:
        print(color)

print_all_colors("red", "blue", "green", "yellow")


#Using **kwargs (Keyword Arguments)
#Use **kwargs for named arguments.
def color_info(**info):
    print("Primary color is", info["primary"])
    print("Secondary color is", info["secondary"])

color_info(primary="red", secondary="orange")


#Function with a List
#A function can take a list as an argument.
def show_colors(color_list):
    for color in color_list:
        print(color)

colors = ["red", "blue", "green"]
show_colors(colors)


#Recursive Function
#A function that calls itself.
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
    else:
        print("Done!")

countdown(3)