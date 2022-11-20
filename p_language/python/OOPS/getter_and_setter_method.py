# getter and setter methods
# getter methods are used to get or return values, also known as accessor methods.
# setter method are used to get or modify the value,also known as muator method.
# Create a class by name Programmer having three field-name,id,technologies
class Programmer:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setId(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setTechnologies(self,techs):
        self.techs=techs
    def getTechnologies(self):
        print(self.techs)

p1=Programmer()
p1.setName("Bishal")
print(p1.getName())
p1.setId(24)
print(p1.getid())
p1.setTechnologies("AI and machine learning")
p1.getTechnologies()

class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setID(self,id):
        self.id=id
    def getID(self):
        return self.id
s1=Student()
s1.setName(["bishal","trupti"])
print(s1.getName())
s1.setID(("arpita","shristi","archanna"))
print(s1.getID())