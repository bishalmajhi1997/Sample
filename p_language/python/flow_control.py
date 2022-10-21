# Flow Control Statements will determine the order in which statements at run time.
#Conditional statements:evaluates until condition is eveluated to true.
# if,if else,if elif else
# control flow structures will make  to  use colon and indentetion.
# Syntex of if statements
# if conditions:
#   code
# if
from tkinter import Y


if 1<2:
    print("yes")
# nested if
if 2<3:
    print("hi")
    if 3>4:
        print("hello")
if 2<3:
    print("hi")
if 3<4:
    print("hello")
# syntax of if else
# if condition:
    # code
# else:
#    else block code
if 2>4:
    print("if block")
else:
    print("else block")
# syntax of if..elif..elif

if 2<4:
    print("true")
elif 3!=3:
    print("elif block")
else:
    print("else bloack")

# elif ladder
name="john"
if (name=="bob"):
    print("hi bob")
elif (name=="bill"):
    print("hi bill")
elif (name=="sam"):
    print("hi sam")
elif (name=="john"):
    print("hi john")
elif(name=="raj"):
    print("hi raj")
else:
    print("what is your name")

# input function()
s=input("What is your name ?")
print(s)
a=input("enter your first name:")
b=input("enter your secodn name")
z=a+b
print(z)
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
z=a+b
print(z)
print(type(z))
x=int(input("enter a number:"))
if x==0:
    print(x,"is zero")
# even and odd
even_odd=int(input("enter your numeber"))
if(even_odd%2==0):
    print("This is even number:",even_odd)
else:
    print("This is odd number:",even_odd)