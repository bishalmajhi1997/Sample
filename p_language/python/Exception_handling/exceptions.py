# Exceptions are run time errors,when our python program is running,if something hoes wrong exception is raised and if we dont haldle those exceptions.
# Property it will cause 3 things
# 1.display informal/unfriendly information to the user
# 2.improper shutdown of resources
# 3.Abnormal termination of program

# try:
#    code that might raise an exception
# except:
    #   catch the exception
# else:
    #   excute with try 
# finally:
#       excutes with try and except
# try:
#     a,b=[int(x) for x in input("Enter two numbers").split()]
#     c=a//b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
#     print("Please enter non zero numbers.")
# print("Code after excutions")


# finally will however excute whether there is error or not.
# try:
#     f=open("file1.txt","w")
#     a,b=[int(x) for x in input("Enter two numbers").split()]
#     c=a//b
#     f.write("writing %d into file"%c)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
#     print("Please enter non zero numbers.")
# finally:
#     f.close()
#     print("file closed.")
# print("Code after excutions")


# try:
#     f=open("file2.txt","w")
#     a,b=[int(x) for x in input("Enter two numbers").split()]
#     c=a//b
#     f.write("writing %d into file"%c)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
#     print("Please enter non zero numbers.")
# else:
#     print("You have entered non zero number.")
# finally:
#     f.close()
#     print("file closed.")
# print("Code after excutions")

try:
    print(x)
except NameError:
    print("Please define the value of x.")

# pravtice questions
# 1.value Error
# import math
# x=int(input("Enter a positive number."))
# try:
#     print(f"square root of {x} is {math.sqrt(x)}")
# except ValueError as e:
#     print(f"you entered number {x} ,which is not positive number")


# 2.Indention Error
# try:
# def f():
# z=["foo","bar"]
# for i in z:
# if i=="foo":
# except IndentationError as e:
# print e
# 3.Attribute Error
class Geeks():
    def __init__(self):
        self.a="geekforgeeks"
obj=Geeks()
try:
    print(obj.a)
    print(obj.b)
except AttributeError:
    print("There is no such attribute")
# 4.Key Error
try:
    a={"a":1,"b":2}
    print(a["c"])
except KeyError:
    print("There is no key c")
