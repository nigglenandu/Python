#A lambda function is a small anonymous function that can have multiple arguments but only one expression.
#Syntax:
#lambda arguments: expression

#Simple Lambda
color = lambda x: x + " is a color"
print(color("red"))  # Output: red is a color


#Multiple Arguments
mix = lambda c1, c2: c1 + " and " + c2 + " make a blend"
print(mix("red", "blue"))  # Output: red and blue make a blend


#Lambda inside a Function
def shade(color_name):
    return lambda shade_level: color_name + " " + shade_level

light_color = shade("blue")
print(light_color("light"))  # Output: blue light


#Using Lambda with map()
colors = ["red", "blue", "green"]
upper_colors = list(map(lambda x: x.upper(), colors))
print(upper_colors)  # Output: ['RED', 'BLUE', 'GREEN']


#Using Lambda with filter()
colors = ["red", "blue", "green", "black", "brown"]
filtered_colors = list(filter(lambda x: "b" in x, colors))
print(filtered_colors)  # Output: ['blue', 'black', 'brown']


#Using Lambda with sorted()
colors = ["red", "blue", "green", "yellow"]
sorted_colors = sorted(colors, key=lambda x: len(x)) 
print(sorted_colors)  # Output: ['red', 'blue', 'green', 'yellow']