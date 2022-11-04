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
# 2.default argument
def average(a=10,b=20):
    c=(a+b)/2
    print(c)
average()
average(a=30,b=40)
# 3.Variable length arguments
def sum(a,b,d,e):
    c=a+b+d+e
    print(c)
sum(3,4,5,6)
print()
def sum(a,*b):#*b means b will hold multiple values
    c=a
    for i in b:
        c=c+i
        print(c)
    print(c)
sum(3,4,5,6)
# 4.Keyword variable length arguments
def person(name,*data):
    print(name)
    print(data)
person("john",30,"delhi",9876,99)
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person("john",age=30,city="delhi",mob=9876,ca=99)
