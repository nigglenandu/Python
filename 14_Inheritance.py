#Inheritance allows one class (child class) to inherit the attributes and methods of another class (parent class).

#Creating a Parent Class:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")


#Creating a Child Class:
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class constructor
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks.")


#Using the Child Class:
dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()  # Buddy barks.


#Using the super() Function: The super() function is used to call methods from the parent class. It allows you to invoke the parent class's methods.
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        print(f"{self.name} meows.")

cat1 = Cat("Whiskers", "White")
cat1.speak()  # Whiskers meows.


#Overriding Methods: In inheritance, a child class can override methods from the parent class.
class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps.")

bird1 = Bird("Parrot")
bird1.speak()  # Parrot chirps.


#The isinstance() Function: You can use isinstance() to check if an object is an instance of a class or a subclass.
animal1 = Animal("Elephant")
print(isinstance(animal1, Animal))  # True
print(isinstance(animal1, Dog))  # False


#Multilevel Inheritance: A child class can inherit from another child class (creating a chain of inheritance).
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def has_hair(self):
        print(f"{self.name} has hair.")

class Whale(Mammal):
    def speak(self):
        print(f"{self.name} makes whale sounds.")

whale1 = Whale("Blue Whale")
whale1.speak()  # Blue Whale makes whale sounds.
whale1.has_hair()  # Blue Whale has hair.


#Hierarchical Inheritance: In hierarchical inheritance, multiple classes inherit from a single parent class.
class Fish(Animal):
    def speak(self):
        print(f"{self.name} swims in the water.")

class Reptile(Animal):
    def speak(self):
        print(f"{self.name} crawls on land.")

fish1 = Fish("Goldfish")
reptile1 = Reptile("Lizard")

fish1.speak()  # Goldfish swims in the water.
reptile1.speak()  # Lizard crawls on land.


'''
Inheritance allows one class to inherit properties and methods from another class.
The child class can override or extend the methods of the parent class.
The super() function is used to call methods from the parent class.
Inheritance supports multilevel and hierarchical inheritance.
'''