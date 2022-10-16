#list is a sequenece/collection which  is ordered and indexed.
#it can store any number of values dynamically.
#list is mutable.
lis=[]
print(lis)
print(type(lis))
st=[10,20,30,"10","python is easy","500",900]
print(st)
print(type(st))

#indexing

print(st[0])
print(st[6])
# print(st[10])index error
print(st[0:6])
print(st[3:8])
print(st[-2:-3])
print(st[-3:-5])
print(st[-5:-2])

#passing stop value
print(st[0:4:2])
print(st[:3:2])

#indexing elements to lists
#append
st.append(40)
print(st)
#extend
st.extend([40.0,9,99.0,"bishal"])
print(st)
#insert
st.insert(3,100)
print(st)
#removing elements from list
st.remove(99.0)
print(st)
#pop
st.pop()
print(st)
st.pop(5)
print(st)
#max and min list elements in the lists
st.remove("10")
print(st)
st.remove("500")
print(st)
print(max(st))
print(min(st))
#sort()
st.sort()
print(st)
st.sort(reverse=True)
print(st)
st.reverse()
print(st)
#length
len(st)
print(len(st))
#copy a list copy(),list()
li=[1,2,3,"12"]
print(li)
li2=li.copy()
print(li2)
li3=list(li2)
print(li3)
#list concatenation
li4=li2+li3
print(li4)
print(["1","3","77"]+li4)
print(["1",3,4]+["1",33,"222","22"])
#list membership text "in" and "not in"
li=["2,",3,"2",10,8,99.8,"string","India","usa"]
print("2" in li)
print(10.0 not in li)
print("india" in li)
print("India" in li)
print("2" and 3 and 4 in li)
print("2" and 3 or "10.0" not in li)
print("2," or 10.0 or "india"not  in li)
print("56" or 3 and "2" or 99 not in li)
#Nested lists
li=["abhishek",2,3,["bishal","shristi"],["kumar",22,333]]
print(li)
print(type(li))
print(li[3][1])
print(li[0][6])
#list concustructor:list(())
print(list(("myphone","mobile","bhusan")))
print(list(("bishal")))
print(list([1,2,3,"bishal"]))
k=[1,2,0,3,2,4,3,"44","888","bishal is very smart boy."]
print(k)
k.append("smruti")
print(k)
k.append(202)
print(k)
k.extend("101")
print(k)
k[4]="6666"
#list is mutable
print(k)
#count
print(k.count(3))
k.clear()
print(k)
del k
a="b,i,shal"
a.split(" ,")
print(a)
print(list(("myphone","mobile","bhusam")))
print(list(("bishal")))
#append(),extend(),insert(),copy(),list(),max(),min(),sort(),count(),index()
#practice questions
#find length of list
#find elements to list
#indexing,slicing
#join two list
#list methods
#copy lists elements

