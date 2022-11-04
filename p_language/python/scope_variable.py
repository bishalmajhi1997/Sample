# Scope of variable
# gloabl variable
# local variable
x=123 #local variable
def display():
    y=456
    print(y)
    print(x)
# print(x)
display()
print(x)
# Accessing global and local variable with same name
a=10
def display():
    a=11#local variable
    print(a)
    print(globals()["a"])#print a global variable inside the functions
print(a)
display()
