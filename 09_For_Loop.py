#A for loop is used to iterate over a sequence (like a list, tuple, or string).
#The for Loop
colors = ["red", "blue", "green"]

for color in colors:
    print(color)


#Looping Through a String
#Strings are iterable, so we can loop through each character.
for letter in "yellow":
    print(letter)


#The break Statement
#break stops the loop when a condition is met.

colors = ["red", "blue", "green", "purple"]

for color in colors:
    if color == "green":
        break  # Stop when "green" is found
    print(color)


#The continue Statement
#continue skips the current iteration.
colors = ["red", "blue", "green"]

for color in colors:
    if color == "blue":
        continue  # Skip "blue"
    print(color)


#Looping with range()
#Use range() to loop a specific number of times.
for i in range(3):
    print("Color:", i)


#The else Block in a For Loop
#The else block runs when the loop finishes normally.
for color in colors:
    print(color)
else:
    print("Loop finished!")


#Nested Loops
#A loop inside another loop.
primary = ["red", "blue"]
secondary = ["green", "purple"]

for p in primary:
    for s in secondary:
        print(p, s)