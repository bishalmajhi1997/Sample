# Function passed as parameter to another parameter.
def display(fun):#main function that has an argument
    return "hi "+ fun
def name():#function to be passed as argument to main function
    return "john"
def show():
    return "How are you ?"
print(display(name()))
print(display(show()))
# Assigning function to variable
a=10
def display():
    b=12
    print(b)
    print(globals()["a"])
print(a)
z=display#assigning function to a variable.
z()#calling/invoking function through variable
# Nested functions
def outer_function(fun):
    def inner_function():
        return "hi"+fun
    return inner_function()
print(outer_function("john"))
# outer function:diplay
# inner function:message
# output:"hi,how are you ?"
def display(fun):
    def message():
        return "hi"+fun
    return message()
print(display(",how are you ?"))
# pass sequenece types to functions:we can pass sequeneces types:list,tuple
def myfunc(lst):
    for i in lst:
        print(i)
myfunc([1,2,3,4])
# even or odd 
def myfunc(lst):
    for i in lst:
        if i%2==0:
            print(i,end=" ")
        # else:
        #     print(i," is odd.")
myfunc([1,2,3,4])

