#Flow control statements will determine the order in which statements at run time.
# conditional statements :evaluates until condition is evaluated to true.
# if,if...else,if..elif..else
# control flow statement will make to use colon and indentetion.
# syntax of if statements
# if condition:
#     code
# nested if
if(2<3):
    print("yes")
    if(3>2):
        print('yes')
# if
if(3<4):
    print("no")
if(4<3):
    print("no")
# syntax of if...else statements
# if condition:
    #  code
# else:
#    code
if(10%2==0):
    print("yes:zero")
else:
    print("nothing")
# syntax of if..elif..else
price=95
if(price>=100):
    print("price is greater than 100")
elif(price<90):
    print("price is less than 90")
else:
    print("nothing")
# ladder statements
salary=29000
if(salary==50000):
    print("salary is high")
elif(salary!=40000):
    print('salary is high')
    if(salary!=2000):
        print("do something")
elif(salary!=25000):
    print("average")
elif(salary!=29000):
    print("best price")
else:
    print("something")
# input
x=input("enter your friends name:")
y=input("enter your best friends name:")
print(x+y)
x=int(input("enter your first semester marks:"))
y=int(input("enter your second semester marks:"))
print(x+y)
