# Types of variables
# There are two types of variables
# 1.Instance Variables
# 2.statice/class variable
class Car:
    color="Black"
    def __init__(self):
        self.make="BMW"
        self.year=2018
        # self.make and self.year are instance variables.
c1=Car()
print(c1.make)
print(c1.year)
print(c1.color)
print(Car.color)
# print(Car.make)Attribute error
Car.color="Red"
print(c1.color)
print(Car.color)

c1.color="White"
print(c1.color)
print(Car.color)

c2=Car()
print(c2.make,c2.year,c2.color)
c2.color="purple"
print(c2.color)
print(Car.color)
Car.color="blue"
print(c2.color)
print(Car.color)
# Create a class named Levelup having three fields-courseName,courseDuration
# Coursefee and access them
# Types of variables
class Levelup:
    Course_fees=23000
    def __init__(self):
        self.CourseName="FSD-1"
        self.CourseDuration="4 months"
class1=Levelup()
print(class1.Course_fees,class1.CourseName,class1.CourseDuration)
print(Levelup.Course_fees)
# print(Levelup.CourseName) attribute error
Levelup.Course_fees=30000
print(Levelup.Course_fees)
print(class1.Course_fees)

class1.Course_fees=35000
print(class1.Course_fees)
print(Levelup.Course_fees)

class2=Levelup()
print(class2.Course_fees,class2.CourseDuration,class2.CourseName)
print(Levelup.Course_fees)

class2.Course_fees=40000
print(class2.Course_fees)
print(Levelup.Course_fees)

Levelup.Course_fees=45000
print(Levelup.Course_fees)
print(class2.Course_fees)
