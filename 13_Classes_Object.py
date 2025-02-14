#A class is a blueprint for creating objects (instances). Objects have properties and behaviors, and classes define them.

#Creating a Class:
class MyClass:
    # Creating a class attribute
    x = 5


#Creating an Object:
# Create an object of the class
obj = MyClass()


# Accessing class attribute
print(obj.x)  # 5


#The __init__() Method: The __init__() method is a special method that is automatically called when an object is created. It is used to initialize the object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an object with parameters
person1 = Person("John", 36)

print(person1.name)  # John
print(person1.age)   # 36


#Object Methods: Methods are functions defined within a class that describe the behaviors of the class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"This car is a {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car1.display()  # This car is a Toyota Corolla


#The self Keyword: The self keyword is used to refer to the instance of the class. It allows access to the attributes and methods of the class.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", 5)
dog1.bark()  # Buddy is barking!


#Class Variables vs Instance Variables:
#Instance variables are variables bound to an instance (object).
#Class variables are shared by all instances of the class.
class Book:
    genre = "Fiction"  # Class variable
    
    def __init__(self, title, author):
        self.title = title  # Instance variable
        self.author = author  # Instance variable

book1 = Book("1984", "George Orwell")
print(book1.title)   # 1984
print(book1.genre)   # Fiction


#Deleting an Object: To delete an object, use the del keyword.
del car1  # Delete the car1 object

'''
A class is a blueprint to create objects.
An object is an instance of a class.
The __init__() method initializes the attributes of an object.
You can define methods to perform actions on the object’s data.
You can use inheritance to reuse code from a parent class.
'''