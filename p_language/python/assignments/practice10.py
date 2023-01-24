#l.Write a Python Program to accept a number and display it is prime or not.
# Ans:
a=int(input("Enter a number:"))
flag=False
if a==1:
    print(f'{a} is not a  prime number.')
elif a>1:
    for i in range(2,a):
        if a%i ==0:
            flag=True
            break
    if flag:
        print(f'{a} is not a prime number.')
    else:
        print(f'{a} is  a prime number.')





#2.Write a Python Program to accept a number and display it is palindrome or not.

b=int(input("Enter a number:"))
k=b
sum=0
while(b>0):
    rem=b%10
    sum=sum*10+rem
    b//=10
if sum==k:
    print(f'{sum} is a palindrome')
else:
    print(f'{sum} is not a palindrome')
#3.Write a Python Program to print "Python Training at Levelup" 15 times using for loop and while loop.
a="Python Training at Levelup"
for i in range(0,15):
    print(a,i)
k=0
while(k<15):
    print(a)
    k+=1
#4.Write a Python program to print fibonacci series less than 100 (0,1,1,2,3,5....89).
a=0
b=1
while(b<100):
    a,b=b,a+b
    print(a,end=" ")
print()
#5.Write a Python Program to accept numbers and display the smallest and greatest number from a set of numbers entered by user.
a=[10,20,30,12,16,19]
# for i in range(len(a)):
#     largest=a[i]
#     smallest=a[i]
#     for j in range(1,len(a)):
#         if smallest
l=a[0]
m=a[0]
for i in range(len(a)):
    if l<a[i]:
        l=a[i]
    if m>a[i]:
        m=a[i]
print(l,m)
print()
#6.Write a Python Program to accept numbers and display the sum of even numbers and odd numbers from a set of numbers entered by the user.
a=[10,20,30,12,16,19]
even=0
odd=0
for i in range(len(a)):
    if a[i]%2==0:
        even+=a[i]
    else:
        odd+=a[i]
print(even,odd)
#7.Write a Python Program to accept numbers and display how many even numbers and odd numbers from a set of numbers entered by the user.
a=[10,20,30,12,16,19]
even_count=0
odd_count=0
for i in range(len(a)):
    if a[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count,odd_count)

#8.Write a Python Program to count all occurences of 'e' in a string.
a="sndnnnfneffmmfeee mf"
count=0
for i in a:
    if 'e' in i:
        count+=1
print(count)

#9.Write a Python Program to check if a Substring is present in a  given string.
b="hdhd dhdh smm dbbf"
c='dh'
if c in b:
    print("yes")
#10.Writa a Python Program to count the number of spaces in the given string.
b="hdhd dhdh smm dbbf"
count=0
for i in b:
    if " " in i:
        count+=1
print(count)
#11.Write a Python Program to input a string and replace every blank space with @ symbol.
b="hdhd dhdh smm dbbf"
count=""
for i in b:
    if " " in i:
        count+="@"
    else:
        count+=i
print(count)

#12.Write a Python Program to count the number of vowels in a string.
a="sbsbbaaaahhshhsbee ii oo uloo dbdbbd dddd"
b="aeiou"
vowel_count=0
for i in a:
    if i in b:
        vowel_count+=1
print(vowel_count)

