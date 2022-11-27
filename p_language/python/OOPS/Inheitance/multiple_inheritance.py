# Types of inheritance
# 1.Single Level inheritance
class A:
    def __init__(Self):
         # super().__init__()
        print("init a")

    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("feature2 is working")
class C:
    def __init__(self):
        super().__init__()
        print("init c")
    def feature5(self):
        print("Feature5 is working.")
class B(C,A):
    def __init__(self):
        super().__init__()
        print("init")
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
    def fature6(self):
        super().feature1()
        print("feature6 is working.")
a=B()
a.feature1()
a.feature2()
a.feature3()
a.feature4()
a.feature5()
a.fature6()