#Everything in python made up of object,
# Objects can be iterable,Thr term iterable means to move over the elements of sequenece.
# for loop is used to make iterations.
# syntax for loop
# myseq=[1,2,3]
# for i in myseq:
#    print(i)
mylist=[1,2,3,4,5,6,7,8,9]
for i in mylist:
    print(i)
# print even numbers in the list
for i in mylist:
    if i%2==0:
        print(i,"is even.")
    else:
        print(i,"is odd")
# add elements in mylist
sum=0
for i in mylist:
    sum+=i
print(sum)
# iterate over strings
tpl=(1,2,3)
for j in tpl:
    print(j)
# create a list of tuples
print()
li=[(1,2,3),(4,5,6),(7,8,9)]
print(li)
print(type(li))
for i,j,k in li:
    print(i,j)
for i in li:
    print(i)
# iterate over directory
d1={1:10,2:20,3:30}
for i in d1:
    print(i)
for i in d1.values():
    print(i)
for i in d1.keys():
    print(i)
for i in d1.items():
    print(i)
for i,j in d1.items():
    print(i,j)
# print numbers 50,70
for i in range(50,70):
    print(i)
for i in range(50,70,4):
    print(i)
# print multiplication table in a given number
num=int(input("enter any number:"))
for i in range(1,11):
    print(i*num)
for i in range(1,11):
    print(i,"X",num,"=",i*num)
