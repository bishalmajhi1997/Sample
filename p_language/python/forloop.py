# everything in python made up of object
# objects can be iterable, The term iterable means to move over the elements of sequence.

# for loop is used to make iterations
# syntax of for loop
# myseq=[1,2,3]
#for i in myseq:
    # print(i)
mylist=[1,2,3,4,5,6,7,8,9]
for i in mylist:
    print(i)
# print even numbers in the list
for i in mylist:
    if(i%2==0):
        print("Even numbers:",i)
    else:
        print("odd numebrs:",i)
# add elements in my list
list_sum=0
for i in mylist:
    list_sum+=i
    # print(list_sum)
print(list_sum)
# iterate over strings
a="hellow world"
for letter in a:
    print(letter,end=" ")
    # print(letter)
print()
for letter in 'python':
    print(letter,'HI')
# iterate over tuple
tpl=(1,2,3)
for i in tpl:
    print(i)
# create a list of tuple
lst=[(1,2),(3,4),(5,6),(7,8)]
print(lst)
print(type(lst))
print(len(lst))
for i in lst:
    print(i)

# tuple unpacking
for t1,t2 in lst:
    print(t1)
    print(t2)

# iterate over directory
d1={1:10,2:20,3:20}
for i in d1:
    print(i)
    print(d1[i])
for i in d1.keys():
    print(i)
for i in d1.values():
    print(i)
for i,j in d1.items():
    print(i,j)
for i in d1.items():
    print(i)
# print number 50,70
for i in range(50,70):
    print(i)
print()
for i in range(50,70,2):
    print(i)
# print multiplication table of a given number.
x=int(input("Enter a number:"))
for i in range(1,11):
    print(i*x)
for i in range(1,11):
    print(x,"X",i,'=',i*x)