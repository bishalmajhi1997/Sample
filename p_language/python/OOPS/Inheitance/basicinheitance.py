# Inheritance is a process of defining new objected using existing objects.
# Inheritance is process of one class inheriting attributes and functionality,
# from another class
# It signifies Ls-A relationship and parent child relationship
# A class that is inherited is known as Parent class/super class/base class.
# A class that is inheritting another class is known as child class/sub class/derived class.

# Implementing new usecase for inheritance
# create a class BMW having attributes-make,model,year,BMW is parent class
# Create two child classes:ThreeSeries having cruiseControlEnabled as its own attribues
# Fiveseries having  parkingAssistEnabled as its own attribute.
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
ts=ThreeSeries("True","BMW","329i",2018)
print(ts.cruiseControlEnabled,ts.make,ts.model,ts.year)

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled
fs=FiveSeries("False","Audi","2212",2022)
print(fs.parkingAssistEnabled,fs.make,fs.model,fs.year)
# 2.create a class School -parent class-name,city
# create a child class -Student-StudentName,Roll no

class School:
    def __init__(self,name,city):
        self.name=name
        self.city=city
class Student(School):
    def __init__(self,studentname,roll_no,name,city):
        School.__init__(self,name,city)
        self.StudentName=studentname
        self.Roll_no=roll_no
    def display(self):
        return self.name,self.Roll_no,self.StudentName,self.city
stu1=Student("Bishal",8,"Level up","Hyderabad")
print(stu1.display())