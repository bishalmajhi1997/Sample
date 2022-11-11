#1.using the reduce function find out the sum of all elements in a list:
#   lst = [5,10,15,20]
#   to use reduce write - 
#   from functools import reduce (import the reduce function)
#2. Write lambda to calculate the sum of two numbers.
#3.create a lambda that will return 'yes' if the given number is even and No if the given number is odd
#4.retrieve odd numbers from given list of numbers using suitable lambda function.
#   lst=[10,2,3,5,7,13,4,8]
# #5.given list of numbers using suitable function add 1 to each element.
#   l1=[2,4,5,6]
#6.write a program to demostrate use of function argument types. 
#7.Demonstrate with an example how functions can be passed as parameter to another function.
# 1.Ans:
lst=[5,10,15,20]
from functools import reduce
sum1=reduce(lambda x,y:x+y,lst)
print(sum1)
# 2.Ans
sum2=lambda x,y:x+y
print(sum2(2,3))
# 3.Ans:
even_odd=lambda x:f"Even number is {x}:yes" if(x%2==0) else f"Odd number is {x}:No"
print(even_odd(5))
# 4.Ans:
lst=[10,2,3,5,7,13,4,8]
lam=list(filter(lambda x:x%2!=0,lst))
print("Odd numbers is :",lam)
for i in lam:
    print(i,end=" ")
# 5.Ans:
print()
l1=[2,4,5,6]
sum1=list(map(lambda x:x+1,l1))
print(sum1)
for i in sum1:
    print(i,end=" ")
# 6.Ans:
def cart(item, price):
   print(item, "cost is :" ,price)

cart(item="bangles", price=20000)
cart(item="handbag", price=100000)
cart(price=1200, item="shirt")
# 7.Ans:
def sum1(a,b):
    return a+b
def sum2(a,b):
    return a-b
print(sum1(sum2(5,4),8))