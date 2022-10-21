#1.Perfrom bitwise operations on 20 and 25.
#2.Demonstarte the use of identity operators with an example
#3.Perform logical operations and comparison operations on 50,55.
# 1.Ans
a=20
b=25
print(a & b)
print(a | b)
print(~a)
print(~b)
print(a>>b)#a/(2^b)
print(a<<b)#a*(2^b)
print(a^b)
# 2.Ans
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
# 3.Ans
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

