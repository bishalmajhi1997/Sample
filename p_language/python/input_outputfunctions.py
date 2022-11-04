# input output function
# print():output functions
# input:input functions
print()
print("hello*3")
print("hello"*3)
print("Python is easy to learn than java")
print("Python is easy to \nlearn than java")
a=10
b=20
print(a,b)
print(a,b,sep=",")
# practice questions
# all operators
# print using format method
name="john"
marks=90.5
print("Name is",name,"Marks are",marks)
print("Name is {} Marks are{}".format(name,marks))
print("Name is {0} and Marks are {1}".format(name,marks))
print(f"Name is {name} and Marks are {marks}")
# input:allows user input
# s=input()
# print(s)
s=input("Enter your name:")
print(s)
# take two numbers from user and multiple them.
a=int(input("Enter your first number:"))
b=int(input("Enter your second numbers:"))
c=a*b
print(c)
print(chr(75))
print(ord("k"))
# Reading charecter
# ch=input("Enter a charecter:")[2]
# print(ch[2])
# print(ch)
# Reading Expression
result=eval(input("Enter an expression:"))
print(result)

# Reading multiple inputs

lst=[int(x) for x in input("Enter multiple values:").split(",")]
print(lst)
print(type(lst))
lst=[float(x) for x in input("Enter multiple values:").split(",")]
print(lst)
print(type(lst))
x,y=[int(x) for x in input("Enter two values:").split()]
print("First number is:",x)
print("Second number is:",y)
# user input using map()
c=map(int,input("Enter multiple values").split())
print(c)
print(type(c))
d=list(map(int,input("Enter multiple values").split()))
print(d)
print(type(d))
d=list(map(float,input("Enter multiple values").split()))
print(d)
print(type(d))
d=list(map(str,input("Enter multiple values").split()))
print(d)
# print(type(d))
# Practice questions
# read character
# read an expression
# read multiple inputs from user