# All methods in abstract are abstract methods.
from abc import ABC,abstractmethod
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
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


