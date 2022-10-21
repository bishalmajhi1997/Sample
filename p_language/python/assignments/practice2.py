# create a set and add a string "python" to set.
#    s={1,2,3,4,5,1,2}
# pop the string from the set,diplayed the pop element,
# ans
s={1,2,3,4,5,1,2}
print(s)
s.add("python")
print(s)
s.pop()
print(s)
s.update([5,6,7])
print(s)
# set concatenation
s1={1,2,3}
s2={4,5,6,4,5}
s3=s1.union(s2)
print(s3)
# find the differences and intersection of below sets.
set1={10,15,"12",10}
set2={"10",10,20,25,30}
set3=set1.difference(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
set3=set2.difference(set1)
print(set3)
set4=set2.intersection(set1)
print(set4)
# create a dictionary using dictionary,constructor
# add item to the dictionary
# remove the last item
d1=dict(moulai="your name",age=23,class1="pg")
print(d1)
d1["passout"]=2022
print(d1)
d1.popitem()
print(d1)
# convert a set into frozen set
s1={1,2,3}
s2=frozenset(s1)
print(type(s2))
k=[1,"st",3]
k.pop(1)
print(k)