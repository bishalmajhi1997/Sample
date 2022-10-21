#Range function returns sequence of numbers,it starts from 0 by default and increment by 1.
r=range(5)
for i in r:
    print(i)
for i in range(1,6):
    print(i,end=" ")
#4,5,6,7,8
print()
k=4
m=9
for i in range(k,m):
    print(i,end=" ")
#5 4 3 2 1
print( )
for m in range(5,0,-1):
    print(m,end=" ")
print()
for x in range(5,0,-1):
    print("Hi",end=" ")
print()
for x in range(7,0,-2):#-2 is step value
    print("x:",x,end=" ")
