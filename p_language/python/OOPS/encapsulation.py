# Encapsulation is binding data and method into a single unit.
# Encapsulation refers to hiding of data from objects.
# Creat a classs by name Student-id,name
from cProfile import Profile


class Student:
    def __init__(self):
        self.id=123
        self.name="Som"
s1=Student()
print(s1.id)
print(s1.name)
# Make fields private by using __ at the begining of the field name
class Student:
    def __init__(self):
        self.__id=123
        self.__name="Som" #self.__id and self.__ are private fields.
s1=Student()
# print(S1.id)
# print(s1.name)
# Access private field using methods
# Access field using name mangling syntax
class Student:
    def __init__(self):
        self.__id=123
        self.__name="Som" #self.__id and self.__ are private fields.
    def display(self):
        print(self.__id)
        print(self.__name)
s2=Student()
print(s2._Student__id)#name mangling syntax
print(s2._Student__name)
s2.display()
print()
# laptop
class Laptop:
    def __init__(self):
        self.__make="Lenovo"
        self.__name="Moulali"
    def display(self):
        print(self.__make)
        print(self.__name)
        return self.__name+" "+self.__make," ".join(self.__name)
lap=Laptop()
lap.display()
print(lap.display())
print(lap._Laptop__make)
print(lap._Laptop__name)
