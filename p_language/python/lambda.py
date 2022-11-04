# Lambda functions are small anonymous function that will not have any name
# syntax of lambda expression
# lambda argument_list:expression
# lambda functions can have multiple arguments,but only one can expressions.
def result(x):
    return x*x
print(result(3))
f=lambda x:(x*x)
print(f(5))
# Lambda function to add two numbers
l=lambda x,y:x+y
print(l(3,4))
l=lambda x,y,z,u:x+y+z+u
print(l(3,4,5,6))
# lambda methods
# filter()-filter out sequenece elements depending on some logic and condition.
# filter(function,iterable)
# Retrive only even numbers from given lists of numbers
lst=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x%2==0,lst))
print(result)
result=list(filter(lambda x:x%2!=0,lst))
print(result)
# map()=maps out sequenece elements depending on some logic and condition
# map(function,iterable)
# In given list double the value of each element
result=list(map(lambda x:x*2,lst))
print(result)
# result=list(filter(lambda x:x*2,lst))
# print(result)
# redude():reduce the sequence elements into single value depending on some logic and some conditions.
# reduce(function,iterable)
# import reduce using -from functools import reduce
from functools import reduce
lst=[5,10,15,20]
result=reduce(lambda x,y:x+y,lst)
print(result)
# Practice questions
# Retrieve numbers dividible by 5 in list
# map 4 to each elements of list
# reduce list=[1,2,3,4] to single value by finding the product.
# nested functions
# Passing any type to function:tuple and print only odd numbers.
# 1.
lst=[5,10,15,22,25,33,35]
def div(a):
    for i in a:
       if(i%5==0):
         print(i,end=" ")
div([5,10,15,22,25,33,35]) 
# 2.
lst=[5,10,15,22,25,33,35]
result=list(map(lambda x:x*4,lst))
for i in result:
     print(i)
# 3.Nested functions
def fun(a):
    def sum(a):
        return a
    return sum(9)
print(fun(3))
# 4.
def odd(a):
    for i in a:
        if i%2 !=0:
            print(i,end=" ")
a=(1,2,3,4,5,6,7,8)
odd(list(a))