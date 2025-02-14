#The datetime module in Python provides classes for manipulating dates and times.

#Importing DateTime
#Import the datetime module to work with date and time.
import datetime


#Getting Current Date and Time
#Use datetime.now() to get the current date and time.
now = datetime.datetime.now()
print(now)  # Output: Current date and time


#Getting Current Date
#Use date.today() to get the current date.
today = datetime.date.today()
print(today)  # Output: Current date


#Creating a Date Object
#Create a date object with year, month, and day.

my_date = datetime.date(2023, 5, 17)
print(my_date)  # Output: 2023-05-17


#Formatting Dates
#Use strftime() to format a date into a string.
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")
print(formatted_date)  # Output: formatted date (e.g., "2023-05-17")


#Parsing Strings to Dates
#Use strptime() to convert a string to a date object.
date_string = "2023-05-17"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)  # Output: 2023-05-17 00:00:00


#Date Arithmetic
#You can subtract dates to get a timedelta object.
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)  # Output: Yesterday's date


#Time Operations
#Use datetime.time() to work with time objects.
time_obj = datetime.time(14, 30, 45)
print(time_obj)  # Output: 14:30:45


#Getting the Current Time
#Use datetime.now() to get the current time.
current_time = datetime.datetime.now().time()
print(current_time)  # Output: Current time


#Getting the Day of the Week
#Use weekday() to get the day of the week (0 = Monday).
today = datetime.date.today()
print(today.weekday())  # Output: Day of the week (0 for Monday)


#Getting the Week Number
#Use isocalendar() to get the week number.
today = datetime.date.today()
print(today.isocalendar())  # Output: (year, week number, weekday)