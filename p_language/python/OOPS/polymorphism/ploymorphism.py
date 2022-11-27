# Polymorphism can be split into two:
# poly-multi/many
# morph-shapes/behaviour/form
# duck typing using polynomial-dynamic passing paramaeters.
class Duck:
    def talk(self):
        print("quick quick")
class Human:
    def talk(self):
        print("Hello")
class Cat:
    def talk(self):
        print("Miiiiiiiiii.")
def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)
e=Human()
callTalk(e)
f=Cat()
callTalk(f)
# Dependency injection using duck typing
# Dependency injection is injection one object into another object as required
class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startengine(self):
        self.engine.start()
class BoingEnginee:
    def start(self):
        print("starting boeing enginee")
class AirBusenginee:
    def start(self):
        print("staring Airbus Enginee")
be=BoingEnginee()
fe=Flight(be)
fe.startengine()

ai=AirBusenginee()
ge=Flight(ai)
ge.startengine()
Flight(BoingEnginee()).startengine()
Flight(AirBusenginee()).startengine()
# Operator overloading-in python operator  can be overloaded to perform multiple opearations
# + is used to perform addition.
# + is used to join listys
# + is used concatenation strings.
a,b=10,2
print(a+b)
lst=[1,2,3]
lst2=[4,5,6]
print(lst+lst2)
s1="python"
s2="iterr"
print(s1+" "+s2)