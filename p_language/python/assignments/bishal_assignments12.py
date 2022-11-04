#1.Write a function to add two numbers using return function.
'''2.Write a program to illustrate functions by taking default parameter as designation = Software Engineer.
call the function and display "Iam working as Software Engineer" (call 3 times everytime changing the designation such as Data Scientist,
data analyst,python developer)'''
#3.write a program to demostrate use of function argument types.
#5.Write a Python function to sum all the numbers in a list.  
# Ans:1.
def add(a,b):
    return a+b
print(add(3,4))
# Ans:2
def designation(designation="Software Engineer"):
    print("I am working as"+" "+designation)
# designation("Software Engineer")
designation("Data Scientist")
designation("Data Analyst")
designation("Python Developer")
# Ans:3
# default arguments
def add(a,b=5,c=10):
    return (a+b+c)
print(add(10))
print(add(3,6))
print(add(3,6,7))
# keyword arguments
def add(a,b=5,c=10):
    return (a+b+c)
print(add(b=10,c=15,a=20))
print(add(a=10))
# Positional arguments
def add(a,b,c):
    return (a+b+c)
print(add(30,40,50))
print(add(10,b=40,c=30))
# Variable length arguments
def add(*a):
    result=0
    for i in a:
        result=result+i
    return result
print(add(1,2,3,4,5))
def add(**a):
    for i  in a.items():
        print(i)
add(number=6,colors="red",fr="apple")
# 5.
def sum(a):
    result=0
    for i in range(len(a)):
        result+=a[i]
    return result
print(sum([1,2,3,4]))