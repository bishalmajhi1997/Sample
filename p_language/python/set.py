#sets are collections which are unordered and unindexed.
#written using {}
#sets does not support multiple items./duplicate items.
from moneyed import M


s={}
print(s)
print(type(s))

s={10,20,40,"xyz",10,20}
print(s)
#sets does not support indexing,slicing,repetition
#Add items to the lists.add(),update()
#add()
s.add(40)
print(s)
s.update([40,50,50,60])
print(s)
#remove items from the set:remove(),discard(),pop()
#remove()
s.remove(20)
print(s)
#discard
s.discard(40)
print(s)
s.discard(70)
print(s)
#pop()
s.pop()
print(s)
s1={"abc",'xyz',"pqr"}
print(s1)
x=s1.pop()
print(x)
print(s1)
#copy set into another set:copy(),set()
s1={1,2,3}
print(s1)
s2=s1.copy()
print(s2)
print(s2)
s3=set(s1)
print(s3)
#join two sets :union(),update()
set1={1,2,3}
set2={4,5,6,88,1}
set3=set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
#length of set
print(len(set1))
print(len(set3))
#issubset
x={"a","b","c"}
y={"f","a","d","b","c","e"}
z=x.issubset(y)
print(z)
x={"a","b","c"}
y={"f","a","d","b","e"}
z=x.issubset(y)
print(z)
x={"a","b","c"}
y={"f","a","d","b","e"}
z=y.issuperset(x)
print(z)
x={"a","b","c"}
y={"f","a","d","b","e","c"}
z=y.issuperset(x)
print(z)
#difference()
x={"apple","fb","microsoft","amazon"}
y={"google","mphasis","cognizent","apple"}
z=x.difference(y)
print(z)
z=y.difference(x)
print(z)
#intersection
s={1,2,3,"1"}
t={1,"1",4}
z=s.intersection(t)
print(z)
#frozensets
#whan a set is converteed intro frozenset:update and remove opearations can not be performed.
#frozensets is immutable.
s={1,2,3}
print(s)
print(type(s))
f=frozenset(s)
print(f)
print(type(f))
# f.update(4) attribute error
# print(type(f))
# f.remove( 3)
# f.clear()
#set constructor-set(())
myset=set(("hi","hello","bye"))
print(myset)
myset.clear()
print(myset)
del myset
li=[1,2,3]
li.clear()
print(li)
m={1,2}
# s={1,2,3,{4,5},{5,6}}type error
# print(s)
# print(myset) Name error
#practice session
#create a set
#add items to the set
#remove items from the set
#find length of set
#convert a set into frozenset
#set methods:copy,difference
#find comma elements from sets
#set constrctor