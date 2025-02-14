'''Polymorphism allows one method or operator to behave differently based on the object it is acting upon. This concept enables a single interface to be used for different data types.

In Python, polymorphism is often achieved through:

Method Overriding - A subclass redefines a method of its superclass.
Method Overloading - Python doesn't support method overloading like some other languages, but it can be simulated using default arguments.
'''

#Method Overriding (Runtime Polymorphism)
#Method overriding occurs when a subclass has a method with the same name as the method in the superclass. The subclass method overrides the superclass method.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the method
animal.sound()  # Animal sound
dog.sound()     # Woof
cat.sound()     # Meow

'''In this example: 
The sound() method is overridden in both the Dog and Cat classes.
The appropriate method is called based on the object (polymorphism in action).
'''


#Operator Overloading
#Polymorphism can also be achieved by overloading operators (e.g., +, -) to work with custom objects.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Creating Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Adding two Point objects
result = point1 + point2
print(result)  # Point(4, 6)
#In this example, the + operator is overloaded for the Point class, allowing the addition of two Point objects.


#Polymorphism with Function Arguments
#Polymorphism is also used when we can pass different object types to a function, and the method will behave differently for each object type.
class Bird:
    def move(self):
        print("Fly in the sky")

class Fish:
    def move(self):
        print("Swim in the water")

def make_move(animal):
    animal.move()

# Creating objects
bird = Bird()
fish = Fish()

# Passing objects of different types to the same function
make_move(bird)  # Fly in the sky
make_move(fish)  # Swim in the water
#Here, the function make_move() works with any object that has a move() method, regardless of its class.

'''
Polymorphism allows different types of objects to be handled using the same interface.
Method overriding allows subclass methods to replace or extend superclass methods.
Operator overloading allows customizing the behavior of operators for user-defined classes.
Function arguments can work with different object types, making the function flexible and reusable.
'''