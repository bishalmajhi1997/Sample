#1.Give an example of multiple variables , multiple assignment and multiple variables single assignment.
#2.with an example demonstrate how to find the memory address of variables
#3.With an example demonstarte how to know the data type of a variable.
#Ans:1.
#a.multiple variable and multiple assignments
a,b,c=10,29,30
print(a,b,c)
#b.mutiple variable and single assignments
a=b=c=10
print(a,b,c)
#Ans:2.
a="string"
b="string"
print(id(a))
print(id(b))
c=b
print(id(c))
d="string2"
print(id(d))
#Ans:3.
a=123
print(type(a))
b="string"
print(type(b))
c=10.4
print(type(c))
d=True
print(type(d))
#output:
# 1. 10 29 30
# 1. 10 10 10
# 2. 2582825939696
# 2. 2582825939696
# 2. 2582825939696
# 2. 2582825767664
# 3. <class 'int'>
# 3. <class 'str'>
# 3. <class 'float'>
# 3.  <class 'bool'>

