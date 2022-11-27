# Abstraction is hiding unnecessary data and focusing on essental data.
# Abstract class will have abstract method.
# Parent class is made as abstrct class
# Abstract method will not have any body.
# Abstraction method will not have any implemetation or body.
# Abstract method can not be Instantiated
from abc import ABC,abstractmethod
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Strating the car")
    def stop(self):
        print("Stoping the car")
    @abstractmethod
    def drive(self):
        pass
class ThreeSeries(BMW):
    def __init__(self,make,model,year,color):
        BMW.__init__(self,make,model,year)
        self.color=color
        print(self.make)
    def start(self):
        print("Button start")
    def stop(self):
        print("Button stop")
    def display(self):
        print(self.color)
    def drive(self):
        print("Three series being driven")
class FiveSeries(ThreeSeries):
    def __init__(self,make,model,year,color,ww):
        BMW.__init__(self,make,model,year)
        self.color=color
        self.ww=ww
    def start(self):
        super().__init__(self.make,self.model,self.year,self.color)
        super().start()
        print("Quite start")
    def stop(self):
        print("Button stop")
    def display(self):
        print(self.color)
    def drive(self):
        print("Five series being driven")
    

ts=FiveSeries("Black","BMW","3281",2022,1)
ts.start()
ts.stop()
ts.display()
ts.drive()


