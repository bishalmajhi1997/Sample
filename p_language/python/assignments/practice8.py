# 1.create a class by name Circle and find the area and perimeter
    #    area=r**2
    #   perimeter=2*pi*r
# 2.Create a class employee and find the avg salary of employee
# 3.Types of inheritance taking employee class/example
# 4.method overriding
# 5.create a inner class Levelup and two inner classes python,html, and access the course name
# Ans 1:
class Circle:
    def __init__(self,r,pi):
        self.pi=pi
        self.r=r
    def area(self):
        area=self.r**2
        return area
    def perimeter(self):
        perimete=self.r*2*self.pi
        return perimete
c1=Circle(3,3.14)
print("Area is ",c1.area())
print("Perimeter is ",c1.perimeter())
# 2.Ans
class Employee:
    def __init__(self,salary):
        self.salary=salary
    def Avg_salary(self):
        avg=sum(self.salary)/len(self.salary)
        return avg
e1=Employee([10,20,30,40,50,60,70,80,90,100])
print("Employee of Average salary is ",e1.Avg_salary())
# 3.Ans
# Single Inheritance
class Employee:
    def __init__(self,empname,bossname):
        self.empname=empname
        self.bossname=bossname
class Boss(Employee):
    def display(self):
        print("Boss name is ",self.bossname,"Employee name is ",self.empname)
e1=Boss("Bishal","Moulali")
e1.display()
# Multiple inheritance
class Employee:
    def __init__(self,empname,bossname,ceoname):
        self.empname=empname
        self.bossname=bossname
        self.ceoname=ceoname
class Boss(Employee):
    def display1(self):
        print("Boss name is ",self.bossname,"Employee name is ",self.empname)
class Ceo(Boss):
    def display(self):
        print("Ceo name is ",self.ceoname)
c1=Ceo("Bishal","moulali","ajeet")
c1.display()
c1.display1()
# Multilevel inheritance
class Employee:
    def __init__(self,empname,bossname,ceoname):
        self.empname=empname
        self.bossname=bossname
        self.ceoname=ceoname
class Boss:
    def display1(self):
        print("Boss name is ",self.bossname,"Employee name is ",self.empname)
class Ceo(Boss,Employee):
    def __init__(self,enpname,bossname,ceoname):
        super().__init__(enpname,bossname,ceoname)
    def display(self):
        print("Ceo name is ",self.ceoname)
c1=Ceo("Bishal","moulalk","ajeet")
c1.display()
c1.display1()
# 4.
class Employee1:
    def __init__(self,empname,bossname,ceoname):
        self.empname=empname
        self.bossname=bossname
        self.ceoname=ceoname
    def display5(self):
        print("Boss name is Bevit.")
class Boss1(Employee1):
    def __init__(self,empname,bossname,ceoname):
        super().__init__(empname,bossname,ceoname)
    def display5(self):
        Employee1.display5(self)
        print("Boss name is ",self.bossname,"Employee name is ",self.empname)
c4=Boss1("sudhakar","gayatri","kajal")
c4.display5()
# 5.Ans
class Levelup:
    class Python:
        def subject1(self,subjectname):
            print("subject name is ",subjectname)
    class Html:
        def subject1(self,subjectname):
            print("Subject name is ",subjectname)
m=Levelup()
n=m.Python()
n.subject1("python")
w=m.Html()
w.subject1("HTML")



