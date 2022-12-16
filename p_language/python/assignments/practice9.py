# 1.multilevel inheritance
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)
    def display(self):
        print(self.a)
class C(B):
    def __init__(self, a, b):
        super().__init__(a, b)
        super().display()
a=C(2,3)
# print(a.a)
a.display()
# 2.
class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
class Child(Parent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def output(self):
        print(self.c)
k=Child(1,2,3)
k.display()
k.output()
# 3.
class Enc:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
    def display1(self):
        print(self.__name,self.__id)
class M(Enc):
    def __init__(self,id,name):
        Enc.__init__(self,id,name)
    def display(self):
        print("nothing")
m=M(44,"bishal")
m.display()
m.display1()
# 4.
class Form1:
    def talk(self):
        print("bdbbd")
class Form2:
    def talk(self):
        print("bbddd")
def talk(obj):
    obj.talk()
k=Form1()
k.talk()
m=Form2()
m.talk()
# 5




