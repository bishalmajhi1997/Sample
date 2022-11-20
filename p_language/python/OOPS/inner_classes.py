# Class inside another class
# Create a class by name Car and inner class enginee and display enginee number.
class Car:
    def __init__(self,make,year):
        Car.make=make
        self.year=year
        
        
    class Enginee:
        def __init__(self,number):
            self.number=number
        def display(self):
            print("Enginee number is:",self.number)
        class Totalprice:
            def __init__(self,price):
                self.price=price
            def Price(self):
                return self.price
    class Vehicle:
        def __init__(self,color):
            self.color=color
        def display(self):
            print(self.color)
c=Car("BMW",1997)
print(Car.make)
c1=c.Enginee(123)
print(c1.number)
print(c.make,c.year)
c1.display()
c2=c1.Totalprice(500000000000)
print(c2.Price())
c4=c.Vehicle("Black")
# c4.display()
# Practice questions
# 1.static method
# 2.create a class Bike and inner  class model and display the model number
class Bike:
    class Model:
        def __init__(self,bike_model):
            self.bikemodel=bike_model
        def display(self):
            return self.bikemodel
bike=Bike()
bike1=Bike.Model("IndianMart")
# print(bike1.display())