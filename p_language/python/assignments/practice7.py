# 1.Write a python program to append a list to a second list.
lst1=[1,2,3,4,5]
lst2=["moulali","Reddy","majhi","abdulla","moulali"]
lst1.extend(lst2)
print(lst1)
# 2.write a python program to sum all item in dictionary.
dic1={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
k=[]
sum=0
for j in dic1.values():
    sum+=j
print(sum)
sum1=0
for k in dic1.keys():
    for n in k:
        m=ord(n)
        sum1+=m
print({str(sum1):sum})
# 3.Write a python function to return all arithmetic operations
def arithmentic(a,b):
    return a+b,a-b,a*b,a//b,a**b,a%b,a/b
print(arithmentic(2,3))
# 4.Write a python program to find largest number among three numbers.
a=2
b=9
c=5
if(a>b and a>c):
    print("Largest number is ",a)
elif(b>c and b>a):
    print("Largest number is ",b)
else:
    print("Largest number is ",c)
# 5.Write a python prgram to calculate length of string with and without len.
st="Python is medium"
print("within length is ",len(st)) 
# st1=st.split(" ")
count=0
for  i in st:
        count+=1
print("without length is ",count)
# 6.write a python program to generate multiplication table of fiven number
a=6
for i in range(15):
    print(i," * ",a," = ",i*a)
# 7.write a python program to print even number i  a list using while loop,for loop, and lambda function
k=[10,11,12,13,14,15,16]
i=0
while(i<len(k)):
    if((k[i]%2)==0):
        print("even numbers is ", k[i])
    i+=1

for i in k:
    if(i%2==0):
        print("even number is ",i)
n=list(filter(lambda k:k%2==0,k))
for i in n:
    print(i,end=" ")
# 8.write apython program to check if a number is prime or not.
print()
a=11
flag=False
for i in range(2,a):
    if(a%i==0):
        flag=True
        break
if flag:
    print(a," is not prime number")
else:
    print(a," is a prime number")
# 9.Split the string whenever  you find instance of separator
# s="life is precious"
s="life is precious"
print(s.split())
# 10.arrange the list in ascending order.
k=[]
lst=[1,2,"cool",-1,0,-3,10]
for i in lst:
    if i is "cool":
        k=0
        for j in i:
            k+=ord(j)
lst.insert(2,k)
print(lst)
lst.remove("cool")
print(lst)
print(sorted(lst))
# 10
k=[]
lst1=[1,2,"cool",-1,0,-3,10]
for i in lst1:
    if i is int:
      k.append(chr(i))
      print(chr(i))



    
