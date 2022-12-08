# pickle module is used to serialize files.
class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def display(self):
        print(self.id,self.name,self.marks)
