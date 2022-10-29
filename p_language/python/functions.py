# function are group of statements that perform specific task.
# functions can be built in or user defined.
# syntax of functions,
# def functionName(arg):
#      function body
# functionname(arg value)
def greet():
    print("key")
    print("hello")
greet()
greet()
# function to add numbers
def add(a,b):
    c=a+b
    print(c)
add(2,3)  #calling/invoking function
# practice questions
# functions to calculate average of two numbers.
# between 1 to 25 print numbers excluding multiplies of 3
# functions to multiply two numbers.
# 1.Ans:
def avg(a,b):
    average=(a+b)/2
    print(average)
avg(33,34)
# 2.Ans
def num(a):
    while(a<24):
        a+=1
        if(a%3==0):
            continue
        else:
            print(a)
num(1)
# 3.Ans:
def mul(a,b):
    c=a*b
    print(c)
mul(5,4)
# function can excute and function can return something.
# function to return average of two numbers.
def avg(a,b):

    return (a+b)/2
print(avg(10,5))
result=avg(10,6)
print(result)
# function to return sum of two integers
def sum(a,b):
    c=a+b
    return c
print(sum(2,7))
# functions can return with multiple values.+,-,*,/
def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u

print(calc(3,5))
for i in calc(10,5):
    print(i)
result=calc(10,5)
for i in result:
    print(i)
# practice questions
# function to add three numbers
# functions to find avg of 2 numbers with and without return
# functions to find area of circle
#    area=pi*r*2
# functions to change first three elements of list
#    lst=[1,2,3,4,5] change 1,2,3 to 10,20,30
# 1.Ans
def add(a,b,c):
    return a+b+c
print(add(11,22,33))
# 2.with return
def avgr(a,b):
    print((a+b)/2)
    return (a+b)/2
print(avgr(3,5))
# 3.Ans

def area(pi,r):
    return pi*r*2
print("Area of circle is ",area(3.14,8))
# 4.
def lst(a):
    a[0]=10
    a[1]=20
    a[2]=30
    return a
print(lst([1,2,3,4,5]))