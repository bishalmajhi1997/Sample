# Transfer statements are used to transfer control from one place to another place
# break,continue,pass
# break:breaks out of current enclosest loop
# continue:goes out to the loop of current enclosest loop
# pass:does nothing at all
# break in for loop
string="python"
for letter in string:
    if letter=="h":
        break
    print(letter)
# break in while loop
# mystring="django"
x=0
while(x<4):
    if x==2:
        break
    print(x)
    x+=1
# print numbers from 1 to  10 and break at 6
print()
for i in range(1,10):
    if(i==6):
        break
    print(i)
x=1
print()
while(x<11):
    if x==6:
        break
    print(x)
    x+=1
# practice questions
# print numbers 20 19 18 17 16 15
# from 20 to 30 print numbers till 25
# in the string "levelup" print only level
# 1.Ans
# using while loop
x=20
while (x>=15):
    print(x)
    x-=1
# using forloop
print()
for i in range(20,15,1):
    print(i)
# 2.Ans
# using while loop
num=20
while(num<30):
    if num==26:
        break
    print(num)
    num+=1
# using for loop
for i in range(num,30):
    if num==26:
        break
    print(num)
# 3.ans
# using for loop
k="levelup"
for i in k:
    if i=="u":
        break
    print(i,end="")
# using while loop
print()
r=0
while (r<len(k)):
    if(k[r]=="u"):
        break
    print(k[r],end="")
    r+=1
# continue:skip the conition
mystr="django"
for letter in mystr:
    if letter=="n":
        continue
    print(letter)
x=0
while x<=20:
    x+=1
    if x%2==0:#skip the even numbers
        continue
    print(x)
# between number 1 to 25 exclude numbers divide by 3
x=1
for i in range(x,25):
    if(i%3==0):
        continue
    print(i)
# while loop
while(x<25):
    x+=1
    if(x%3==0):
        continue
    else:
        print(x)
    # x+=1
# pass
x=[1,2,3]
for i in x:
    pass
print("end of scripts")
for i in range(1,25):
    if i%2==0:
        pass
    else:
        print(i)
# for else
x=[10,20,333,11,15]
for i in  x:
    if(i%5==0):
        print(i)
        break
x=[11,12,13,14,15,16,18,19]
for i in x:
    if i%5==0:
        pass
    else:
        print("not found")
else:
    print("not found again")
# check if the number is prime or not.
num=7
for i in range(2,num):
    if(num%2==0):
        print("not prime")
        break
else:
    print("prime")