# Method Overrieding
# inheriting functionality/method
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    def start(self):
        print("Button start")
    def stop(self):
        print("Button stop")
ts=ThreeSeries("True","BMW","329i",2018)
print(ts.cruiseControlEnabled,ts.make,ts.model,ts.year,ts.start(),ts.stop(),ts.display())
ts.start()
ts.stop()
class School:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def meth(self):
        print("Python,html")
class StudentName(School):
    def __init__(self,stuname,roll_no,name,city):
            School.__init__(self,name,city)
            self.cityname=stuname
            self.roll_no=roll_no
    def meth(self):
        print(self.roll_no)
        print(self.cityname)
s1=StudentName("bishal",120,"MMM","Hyderabad")
print(s1.cityname,s1.city,s1.name,s1.roll_no)
s1.meth()
# Prevent method overriding
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Starting the car")
    def stop(self):
        print("stopping the car.")
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
    def start(self):
        super().start()
        print("Button satrt.")
    def stop(self):
        super().stop()
        print("Button stop.")
    def display(self):
        print(self.cruiseControlEnabled)
ts1=ThreeSeries("True","BMW","3series",2018)
ts1.start()
ts1.stop()
ts1.display()

class Student:
    def __init__(self,name,rollno,percentage):
        self.name=name
        self.rollno=rollno
        self.percenatge=percentage
    def percentage1(self):
        print(self.percenatge)
    def totalmarks(self):
        print("Total marks is ",self.rollno)
class College(Student):
    def __init__(self,collegename,collegestudenttotal,name,rollno,percentage):
        super().__init__(name,rollno,percentage)
        self.collegename=collegename
        self.collegestudentotal=collegestudenttotal
    def percentage1(self):
        super().percentage1()
        print("Total percenatge")
    def totalmarks(self):
        super().totalmarks()
        print("total marks")
c1=College("GITA Autonomous college",4000,"Bishal kumar majhi",111,99)
c1.percentage1()
c1.totalmarks()
print(c1.collegename,c1.name,c1.rollno)
# Practice questions
# method overriding
# using super()

