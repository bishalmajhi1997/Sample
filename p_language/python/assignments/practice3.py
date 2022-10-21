# create list of element list=[1,2,3,10,15,20,15] .print multiply of 5
list1=[1,2,3,10,15,20,15]
k=len(list1)
for i in range(0,k):
    if(list1[i]%5==0):
        print(list1[i])
# votes
age=int(input("Enter your age:"))
if(age>=18):
    print("He/She is eligible.")
else:
    print("not eleigible.")
for i in range(0,50):
    if(i%3==0 or i%5==0):
        print(i)