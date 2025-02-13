# String in Python
# A string is a sequence of characters enclosed in quotes.

mystring = "hello"
print(mystring)  # Output: hello
print(len(mystring))  # Length of string
print(type(mystring))  # Type of variable


#Accessing Characters
print(mystring[1])  # 'e' (Access by index)
print(mystring[-1])  # 'o' (Negative indexing - last character)
print(mystring[1:4])  # 'ell' (Slicing)


#Modifying Strings
#Convert to Upper and Lower case
print(mystring.upper())  # 'HELLO'
print(mystring.lower())  # 'hello'

#Remove Whitespaces
text = "  hello  "
print(text.strip())  # 'hello' (Removes spaces)

#Replace Characters
print(mystring.replace("h", "y"))  # 'yello'

#Split a String
text = "red,blue,green"
print(text.split(","))  # ['red', 'blue', 'green']

#Concatenation (Joining Strings)
first = "Hello"
second = "World"
print(first + " " + second)  # 'Hello World'


#Loop Through a String
for char in mystring:
    print(char)  # Prints each character


#Check if Substring Exists
text = "hello world"
print("hello" in text)  # True
print("bye" not in text)  # True


#String Formatting
#Using f-strings (Python 3.6+)
name = "Niggle"
age = 25
print(f"My name is {name} and I am {age} years old.")

#Using .format() Method
print("My name is {} and I am {} years old.".format(name, age))

#Using % Operator
print("My name is %s and I am %d years old." % (name, age))


#Escape Characters
print("She said \"Hello!\"")  # She said "Hello!"
print("Line1\nLine2")  # New line
print("Tab\tSpace")  # Tab space
