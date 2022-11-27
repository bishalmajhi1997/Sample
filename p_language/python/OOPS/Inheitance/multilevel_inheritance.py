# Types of inheritance
# 2.Multi Level inheritance
class A:
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class C(B):
    def feature5(self):
        print("feature5 is working")
a=B()
a.feature3()
a.feature4()
a.feature1()
a.feature2()
a.feature5()