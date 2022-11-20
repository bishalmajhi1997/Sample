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
ts=ThreeSeries("True","BMW","329i",2018)
print(ts.cruiseControlEnabled,ts.make,ts.model,ts.year,ts.start(),ts.stop(),ts.display())
# practice questions
# Creat a class school-parent class -name,city and methods python html
# create a child class -student-studentname,roll_no and method displaying studentname and roll_no.
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
    def meth1(self):
        print(self.roll_no)
        print(self.cityname)
s1=StudentName("bishal",120,"MMM","Hyderabad")
print(s1.cityname,s1.city,s1.name,s1.roll_no)
s1.meth()
s1.meth1()
