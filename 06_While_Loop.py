#A while loop keeps running as long as the condition is True.

color = "red"
count = 0

while count < 3:
    print(color)  
    count += 1  


#The break Statement
#break stops the loop when a condition is met.
colors = ["red", "blue", "green"]
index = 0

while index < len(colors):
    if colors[index] == "blue":
        break  # Stop when "blue" is found
    print(colors[index])
    index += 1  


#The continue Statement
#continue skips the current iteration and moves to the next.
colors = ["red", "blue", "green"]
index = 0

while index < len(colors):
    if colors[index] == "blue":
        index += 1
        continue  # Skip printing "blue"
    print(colors[index])
    index += 1  


#The else Block in a While Loop
#The else block runs when the loop finishes without a break.
count = 0

while count < 3:
    print("Looping:", count)
    count += 1
else:
    print("Loop finished!")  


#Infinite Loop (Use with Caution!)
#An infinite loop runs forever unless stopped.
while True:
    print("This is an infinite loop.")
    break  # Use 'break' to stop it
