#Range function returns a sequenece of numbers,it starts from 0 by default and increment by 1.
r=range(5)
for i in r:
    print(i)
print()
for i in range(1,7):
    print(i,end=" ")
print()
#4,5,6,7,8,9
for i in range(4,10):
    print(i,end=" ")

#5,4,3,2,1
print()
for i in range(5,0,-1):
    print(i,end=" ")
print()
for x in range(7,2,-2):
    print("hi:",x,end=" ")