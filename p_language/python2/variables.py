#variables are box containers for storing values.
x=10
print(x)
x="john"
print(x)
#case sensitivity
name="levelup"
Name="Levelup"
NAME="LEVELUP"
print(name,Name,NAME)
#we can not have constant variable in pythons.
pi=3.142
print(pi)
pi=2.321
print(pi)
#more on variables
b=10
a=b
print(a)
print(b)
print(id(a))
print(id(b))
a=11
print(a)
print(id(a))
#multiple variables,single assignments
a=b=c=8
print(a,b,c)
a,b,c=8,9,0
print(a,b,c)
a=20
print(type(a))