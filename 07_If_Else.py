#An if statement runs a block of code only if the condition is True.

#if statement
color = "blue"

if color == "blue":
    print("The color is blue.")  # Output: The color is blue.
 

#The if-else Statement
#The else block runs if the if condition is False.
color = "red"

if color == "blue":
    print("The color is blue.")
else:
    print("The color is not blue.")  # Output: The color is not blue.


#The if-elif-else Statement
#Use elif to check multiple conditions.
color = "green"

if color == "blue":
    print("The color is blue.")
elif color == "red":
    print("The color is red.")
elif color == "green":
    print("The color is green.")  # Output: The color is green.
else:
    print("Unknown color.")


#Using Logical Operators (and, or, not)
#Using and
#Both conditions must be True.
color1 = "red"
color2 = "blue"

if color1 == "red" and color2 == "blue":
    print("Red and blue make purple.")  # Output: Red and blue make purple.

#Using or
#At least one condition must be True.
if color1 == "red" or color2 == "green":
    print("One of the colors is red or green.")  # Output: One of the colors is red or green.

#Using not
#Negates the condition.
if not color1 == "green":
    print("Color1 is not green.")  # Output: Color1 is not green.


#Nested if Statements
#An if inside another if.
color = "blue"
shade = "dark"

if color == "blue":
    if shade == "dark":
        print("The color is dark blue.")  # Output: The color is dark blue.


#Checking Membership in Lists
colors = ["red", "blue", "green"]

if "blue" in colors:
    print("Blue is in the list!")  # Output: Blue is in the list.
