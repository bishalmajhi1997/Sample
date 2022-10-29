# write a python program that accepts two numbers and calculate the product.
a=int(input("enter a number"))
b=int(input("enter a second number"))
# def mul(a,b):
#     a=int(input("enter a number"))
#     b=int(input("enter a second number"))
c=a*b
    # return c
print(c)

# write a python program to reverse the string
#   mystr="python at levelup"
mystr="python at levelup"
print(mystr[::-1])
# m=""
# for i in range(len(mystr)):
#     m+=mystr
# print(m)
# write a python program to calculate area of circle pi=3.14
r=float(input("Enter number:"))
pi=3.14
print("Area of circle is %.2f:"%(pi*r**2))
# WAP to represent 25 in different formats.
a=25
print(hex(a))
print(oct(a))
print(bin(a))
# print(str(a))
# print(float(a))
print(round(a))
# WAP to print the below string.
# s=("python" "at" "levelup")
# output should be python@@at@@levelup
s=("python","at","levelup")
# print("python","at","levelup",sep=("@@"))
s=list(s)
print("@@".join(s))
    