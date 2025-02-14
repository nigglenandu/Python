#The math module provides mathematical functions and constants to perform mathematical operations in Python.

#Importing the Math Module
import math

#Pi Constant
#Use math.pi to get the value of pi.
print(math.pi)  # Output: 3.141592653589793


#Square Root
#Use math.sqrt() to get the square root of a number.
print(math.sqrt(16))  # Output: 4.0

#Power
#Use math.pow() to calculate the power of a number.
print(math.pow(2, 3))  # Output: 8.0


#Rounding
#Use math.ceil() to round a number up and math.floor() to round a number down.
print(math.ceil(4.2))  # Output: 5
print(math.floor(4.7))  # Output: 4


#Absolute Value
#Use math.fabs() to get the absolute value of a number.
print(math.fabs(-5))  # Output: 5.0


#Trigonometric Functions
#You can use trigonometric functions like sin(), cos(), tan() (angles in radians).
print(math.sin(math.pi / 2))  # Output: 1.0

#Exponential and Logarithmic Functions
#Use math.exp() for exponentiation and math.log() for logarithms.
print(math.exp(2))  # Output: 7.3890560989306495
print(math.log(100, 10))  # Output: 2.0


#Factorial
#Use math.factorial() to calculate the factorial of a number.
print(math.factorial(5))  # Output: 120


#Greatest Common Divisor (GCD)
#Use math.gcd() to find the greatest common divisor of two numbers.
print(math.gcd(24, 36))  # Output: 12


#Angle Conversion
#Use math.radians() to convert degrees to radians and math.degrees() to convert radians to degrees.
print(math.radians(90))  # Output: 1.5707963267948966
print(math.degrees(math.pi / 2))  # Output: 90.0