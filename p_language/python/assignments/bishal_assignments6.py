#1.use a set to find the unique values of list :

 #mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]

'''2.Given a set,demostrate the use of copy().

   s={"fb","insta","twitter","whatsapp"}''' 

#3.create set and demonstrate the use of difference(),issubset(),issuperset(),intersection.

#4.create a set and convert it into frozenset.

#5.show how two sets can be joined with an example.
# 1.Ans
mylist= [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
print(set(mylist))
# 2.Ans
s={"fb","insta","twitter","whatsapp"}
m=s.copy()
print(m)
# 3.Ans:
a={1,2,3,"1","bishal","kumar","majhi"}
b={2,3,1,"2","moulali","ajit","majhi"}
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
print(b.intersection(a))
m=a.issuperset(b)
print(m)
a={1,2,3,"abhi"}
b={2,4,1,3,"abhi","suresh"}
print(b.issuperset(a))
print(a.issubset(b))
# 4.Ans
set1={"bishal","kumar","siku",1,2,3}
set1=frozenset(set1)
print(type(set1))
# 5.Ans
set1={"fruit","mango","apple","veg","non-veg"}
set2={"washington","fuzi","gala","kashmir","golden apple"}
print(set1.union(set2))
set1.update(set2)
print(set1)