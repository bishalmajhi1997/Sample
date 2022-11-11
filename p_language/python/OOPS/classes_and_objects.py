# Python is an object oriented programming language.
# In python everything is made up of objects
# Objects are instance of class.
# Objects will have 3 things.
# 1.Name/identity
# 2.attributes/properties/variables/fields
# 3.behavior/functionality
# OOPs principles
# 1.Encapsulation
# 2.Inheritance
# 3.1polymorphism
# 4.Abstraction
# Classes are sketch/blueprint/design for objects
# Classes will have data,variables,functions/methods.
# Create a class named product,having three variables-name,description,price
class Product:
    def __init__(self):#__init__ is built constructor method
        self.name="phone" #self points to current object creation
        self.description="its awesome"
        self.price=8000
p1=Product()#Object is created and constructor is invoked
#To access fields
print(p1.description)
print(p1.price)
print(p1.name)
# Car-make,model,year
class Car:
    def __init__(self) :
        self.make="Bishal"
        self.model="Audi"
        self.year="year"
car=Car()
print(car.make)
print(car.model)
print(car.year)
car2=Car()
print(car2.make)
print(car2.model)
print(car2.year)