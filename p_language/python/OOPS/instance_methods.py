# Instance method
# Write a python class to calculate average rating of course
class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def average(self):#instance method
        numberofratings=sum(self.ratings)/len(self.ratings)
        print("Average ratings of",self.name,"is:",numberofratings)
        return numberofratings
c1=Course("Python",[1,2,3,4,5])
print(c1.ratings)
print(c1.average)
print(c1.average())
# Practice questions
# Types of methods
# Instance method
# Class method
