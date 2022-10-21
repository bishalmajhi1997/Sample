# 1.reverse the list.
# lst=[9,8,7,6,5]

# add element 3,2,1 to the list.
# sort lst in descending order
# reverse the last element from the list
from copy import copy


lst=[9,8,7,6,5]
k=lst[::-1]
print(k)
k.extend([3,2,1])
print(k)
k.sort(reverse=True)
print(k)
k.pop()
print(k)
#2.below create a tuple and copy element of it.
# x=('bmw','audi','jaguar')
# change "audi" to "benz"
# find the index of "bmw"
x=("bmw","audi","jaguar")
y=copy(x)
print(y)
y=list(y)
y.insert(1,"benz")
print(y)
print(tuple(y))
print(y.index("bmw"))
# in the given string
# s="levelup"
# print 'elup','up','p'
s="levelup"
print(s[3:])
print(s[5:])
print(s[6:])
# print the output "python at levelup" using concatenation
x="python"
y="at"
z="levelup"
print(x+" "+y+" "+z)