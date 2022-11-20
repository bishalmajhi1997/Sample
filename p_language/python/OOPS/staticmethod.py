# static method
# define statice method and static file
# create a class and count the number of objects created and display them.
class ObjectCounter:  
    numberOfobjects=0#statice field
    def __init__(self):
        ObjectCounter.numberOfobjects+=1
    @staticmethod
    def display():
        print(ObjectCounter.numberOfobjects)
o1=ObjectCounter()
o2=ObjectCounter()
obj=ObjectCounter()
ObjectCounter.display()
