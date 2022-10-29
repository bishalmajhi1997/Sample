# Types of arguments
def add(a,b):#a,b are known as formal arguments
    print(a+b)
add(2,3)#2,3 are known as actual arguments
# Actual arguments are of 4 types
# 1.position arguments
# 2.default arguments
# 3.variable length arguments
# 4,keyword variable length arguments
# 1.position arguments
def person(name,age):
    print(name)
    print(age)
person("john",27)
person(age=80,name="sam")
person(80,"bishal")
def frnd(name,address):
    print(name)
    print(address)
frnd("moulali",["ap",999999,"guntur"])
frnd(address="moulali",name=[11,2,33,"vv"])