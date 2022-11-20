# Parameter constructor:Constructor with parameters/arguments
class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
c1=Course("Java",(1,2,3,4,5))
print(c1.name)
print(c1.ratings)
c2=Course("Python",[1,2,3,4,5]  )
print(c2.name)
print(c2.ratings)
# Create a class named student passing name,id and marks and accessing them 
# Create two object instance
class Student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks
class1=Student("Bishal","MCA",91.23)
print(class1.name,class1.id,class1.marks)
class2=Student("Moulali","MSc",97.12)
print(class2.name,class2.id,class2.marks)