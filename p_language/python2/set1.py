#sets are collection which is unordered/unindexed.
#written using {}
#set does not support multiple items,/duplicate items.
s={}
print(s)
print(type(s))
s={10,20,30,40,"50","88"}
print(s)
print(type(s))
#set does not support slicing,indexing,repetitions.
#add items to the list.set(),update()
#add()s
s.add(33)
print(s)
s.update([10,22,33])
print(s)
#remove the items from the set.
#remove
s.remove(33)
print(s)
s.discard(23)
print(s)
s.pop()
print(s)
#copy set into another set.#copy(),set()
k=s.copy()
print(k)
n=set(s)
print(n)
#join two sets:union(),update()
a={1,2,3,4}
b={"abhu","bahu","monika","kajal"}
print(a.union(b))
a.update(b)
print(a)
#length of set
print(len(a))
print(len(b))
#issuperset()
a={1,2,3,4,5}
b={1,2,3}
c=a.issuperset(b)
print(c)
c=b.issuperset(a)
print(c)
c=a.issubset(b)
print(c)
c=b.issubset(a)
print(c)
#differenec
k=a.difference(b)
print(k)
m=b.difference(a)
print(m)
m=a.intersection(b)
print(m)
m=b.intersection(a)
print(m)
#frozenset:when a set is coverted into frozenset:remove(),update() operations can not be performed.
#frozen sets is immutable
a=frozenset(a)
print(a)
print(type(a))
#set constrctor
a=set(("abhi","gayatri"))
print(a)
print(type(a))
a.clear()
print(a)
del a