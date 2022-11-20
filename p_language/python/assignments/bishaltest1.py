# 1.In the given tuple add "India"
#    tuple("usa"."uk","canada")
# 1.Ans
tpl = ("usa", "uk", "canada")
tpl = list(tpl)
tpl.append("India")
print(tuple(tpl))

# 2.Reverse the string
#    s="Python training at Levelup"
# 2.Ans:
s = "Python training at Levelup"
print(s[::-1])
# 3.print numbers divisible by 3 and 5 between 1 to 100.
# 3.Ans:
for i in range(100):
    if (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")
# 4.write a python program to print odd numbers in a range.
# 4.Ans:
print()
for i in range(100):
    if(i%2 !=0):
        print(i,end="")
# 5.Write a python program to generate multiplication table of a given number.
#  5.Ans
n=9
for i in range(1,30):
    print(i,"*",9,"=",i*9)
# 6.A person named Sahil,as a citizen of nation has a right to vote.
# Considering minimum age to vote write a function in python that he is  eligible to votes.
# 6.Ans:
sahile_age=38
def age(sahile_age):
    if(18<sahile_age):
        print("He is eligible for vote")
age(sahile_age)
# 7.Ans
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
# 8.ans:
john=["python","java","django","html"]
john.sort(reverse=True)
print(john)
if len(john[1])<len(john[3]):
    print("He required basic knowledge of css that could be least prioritized how do you help john with this.")
# 9.Ans:
lst=[1,2,3,4,5,6,7,8,9]
odd_n=list(filter(lambda x:x%2!=0,lst))
# print(odd_n)
for i in odd_n:
    print(i,end=" ")
# 10.Ans:
a=5
print(float(a))
a=(1,2,3)
print(set(a))
a="1"
print(int(a))

