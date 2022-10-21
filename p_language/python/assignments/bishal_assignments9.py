'''1.Write a Python program to find the Area of Triangle.
   semi-perimeter : s=(a+b+c)/2
  (formula to find area of traingle  is area = (s*(s-a)*(s-b)*(s-c))**0.5)'''

'''2.Write a Pyhton program to capture employee details like emp_id,emp_name and emp_salary
  # and display them.'''
  
#3.Write a program to calculate the average of three numbers taking user input.
'''4.Write a program to calculate the compound Interest.
   CI=P(1+R/100)^t'''
   
#5.Write a program to represent integer 20 into binary,hexadecimal and octal.
#6.Write a program to calculate square root of a number. (square root = number ** 0.5)
'''7.Write a program to calculate Simple Interest by taking user input
    si=(p*t*r)/100'''
#8.Write a program to calculate the Area of circle using math module
#6.Perfrom bitwise operations on 20 and 25.
#7.Demonstarte the use of identity operators with an example
#8.Perform logical operations and comparison operations on 50,55.
#9.Demonstrate the following with example
#    1.reading an expression
#    2.reading char
#    3.reaading multiple inputs
#    4.use of format method
# 1.Ans:
a=float(input("enter a number:"))
b=float(input("enter a number:"))
c=float(input("enter a number:"))
s=(a+b+c)/2
print(s)
Area_of_triangle= ((s*(s-a)*(s-b)*(s-c))**0.5)
print("Area of Triangle:",Area_of_triangle)
# 2.Ans:
emp_id=int(input("enter employee id:"))
emp_name=input("enter employee name:")
emp_salary=float(input("enter employee salary:"))
employee=str(emp_id)+" "+emp_name+" "+str(emp_salary)
print("Employee details:",employee)
print("Employee details emp_id:{} ,emp_name:{} ,emp_salary:{}".format(emp_id,emp_name,emp_salary))
# 3.Ans:
a=float(input("enter your first numbers:"))
b=float(input("enter your second numbers:"))
d=float(input("enter your third numbers:"))
print("Average of three numbers:",(a+b+d)/2)
# 4.Ans:
P=float(input("Enter principal amount:"))
R=float(input("Enter rate of Interest:"))
T=float(input("Enter Time period in years:"))
a=(P*(1+(R/100)))**T
CI=a-P
print("Compound Interest:",CI)
# 5.Ans
print(bin(20))
print(hex(20))
print(oct(20))
# 6.Ans
number=float(input("enter number:"))
square_root=number*0.5
print("Square root:",square_root)
# 7.Ans
p=float(input("enter  principal amount:"))
r=float(input("enter rate of interest:"))
t=float(input("enter time period in years:"))
si=(p*t*r)/100
print("Simple interest:",si)
# 8.Ans
PI=3.14
r=float(input('Enter radius:'))
area=PI*(r**2)
print("Area of Circle:",area)
print("bishal"*3)
# 6.Ans
print(20 & 25)
a=20
b=25
print(a & b)
print(a | b)
print(~a)
print(~b)
print(a>>b)#a/(2^b)
print(a<<b)#a*(2^b)
print(a^b)
#7 Ans:
a=[1,2,3]
b=2
for i in range(len(a)):
    if a[i] is b:
        print(a[i])
    else:
        print("nothing")
a=["bishal",'kumar',1,2,3]
print()
b="kumar"
for j in range(len(a)):
    if a[j] is not b:
        print("nothing")
    else:
        print(a[j])
 
# 8.Ans
a=50 
b=55
if a and b:
    print("a and b") 
    if a or b:
       print("a or b")
       if  a:
         print("a")
         if  not b:
            print(b)
if(a==b):
    print("a is equal to b")
elif(a!=b):
    print("a is not equal to b")
    if(a<b):
      print("a is less than b")
      if(a<=b):
         print("a is less or equal to b")
         if(a>=b):
           print("a is greater or equal to b")
    elif(a>b):
        print("a is greater than b")
    else:
       print("nothing")

