from re import A


print("kumar")
#variable are box/container for storing values
x=10
print(x)
x="john"
print(x)
#case sensitivity
name="bishal"
Name="Bishal"
NAME="BISHAL"
print(name,Name,NAME)
#WE can not have const variables in python.
pi=3.142
print(pi)
pi=3.142
print(pi)
#more on variables
a=10
b=a 
print(a)
print(b)
#id returns memory address of variable;
print(id(a))
print(id(b))
c=10
print(c)
print(id(c))
a=11
print(a)
print(id(a))
#Types of variable assignment
#1.Multiple variables,Single assignments
a=b=c=5
print(a,b,c)
#2.Mum=ltiple variable,multiple assignments
a=1
b=2
c=3
# a,b,c=5,6,7,8#value error
a,b,c=5,6,7
print(a,b,c)
#types and value
a=200
#a is variable and 200 is value
print(a)
print(type(a))
#python supports wide range of data types
#1.None type
a=None
print(a)
print(type(a))
#2.Numeric types-int,float,complex numbers
a=10
print(a)
print(type(a))
a=10.23
print(a)
print(type(a))
a="10"#numeric string
print(a)
print(type(a))
a="python is easy"
print(a)
print(type(a))
#3.complex data types
a=1+2j#1 is real part,2j is imaginary part and j is standard co-efficient.
print(a)
print(type(a))
#4.booleans
a=True
print(a)
print(type(a))
print(3<2)
#5.Represent number in different format-binary,hexadecimal,octal
print(bin(10))
print(hex(45))
print(oct(43))
#type conversion(type casting)-coverting one data type into another
#1.convert a floating point number to integer
a=10.5
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
#2.conert a integer to float
a=10
print(a)
print(type(a))
b=float(a)
print(b)
print(type(b))
#2.conert a string to int
a="10"
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))#charecter string does not support.
#practice
#define variable
#variable assignments
#check the address of variable
#representation of number different formats
#type conversion
#check the types of variables
#examples of different types of variables.
