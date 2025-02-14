#try-except is used for exception handling, allowing you to handle errors gracefully without crashing the program.

#Basic Try Except
try:
    x = 10 / 0  # Division by zero
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Handling Multiple Exceptions:
try:
    x = int("hello")  # ValueError
except (ValueError, ZeroDivisionError):
    print("An error occurred!")


#Else Clause (Runs if no exceptions are raised):
try:
    x = 10 / 2  # No error
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")


#Finally Clause (Always runs):
try:
    x = 10 / 2  # No error
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run!")