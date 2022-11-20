# Types  of methods
# There are 3 types of methods
# !.Instance method
# 2.class method
# 3.static method
class Student:
    School="ABC"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):#instance method will take self as argument
            print("Average is:",(self.m1+self.m2+self.m3)/3)
    @classmethod
    def info(clss):#class method will take clss as argument
        return clss.School
    @staticmethod
    def display():#static method will not have anytinh inside the bracket
        print("This is static method.")
s1=Student(100,200,300)
print(s1.m1)
print(s1.m2)
print(s1.m3)
s1.average()
print(s1.info())
s1.display()
class Employee:
    Emp_salary=400000
    def __init__(self,s1,s2,s3,s4):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
    def Salary_sum(self):
        return self.s1+self.s2+self.s3+self.s4
    @classmethod
    def Salary_avg(cl):
        return cl.Emp_salary
    @staticmethod
    def average():
        return Employee.Emp_salary
emp1=Employee(10000,20000,3000,40000)
print(emp1.s1)
print(emp1.s2)
print(emp1.s3)
print(emp1.s4)
print(emp1.Salary_sum())
print(emp1.Salary_avg())
print(emp1.average())