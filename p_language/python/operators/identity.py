#Identity operators are used to check if objects are same with same memory location
#'is' and 'is not'

x=[1,2,3]
y=[1,2,3,4]
y=x
print(x==y)
print(x is y)
z=x
print(z is x)
print(z is not x)


#tuples
a=(1,2,3)
b=(1,2,3)
print(a is b)
print(a is not b)