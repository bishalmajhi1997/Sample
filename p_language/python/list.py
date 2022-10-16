#List is a sequence/collection which is ordered and indexed.
#it can store any number of values dynamically.
#it is mutable.
#written using[]
lis=[]
print(lis)
print(type(lis))
st=[10,20,30,'python',-30,30,2]
print(st)
#indexing
print(st[0])
print(st[4])
print(st[-3])
# print(st[-9])#indexerror
print(st[0:4])
print(st[2:])
print(st[:3])
print(st[-2:-3])
print(st[-1:-3])
print(st[-3:-1])
#passing stop value
print(st[:4:2])
print(st[::-1])
#indexing elements to list
#append()
st.append(50)
print(st)
#insert()
st.insert(3,90)
print(st)
#extend()
st.extend([88,99,"bdbbd"])
print(st)
#removing elements from list
#remove
st.remove("bdbbd")
print(st)
#pop()-remove last elements
st.pop()
print(st)
#pop(index)
st.pop(4)
print(st)
# st.remove("-30")
print(st)
#max and min elements in the list
print(max(st))
print(min(st))
#sort()
st.sort()
print(st)#ascending order
st.sort(reverse=True)#descending order
print(st)
#length of list
print(len(st))
#repetition
print(st*2)
#copy a list-copy(),list()
li=[1,2,3]
print(li)
li=li.copy()
print(li)
li2=list(li)
print(li2)
#list concatenation
list=[1,2,3]
list2=[4,5,6]
st=list+list2
print(list+list2)
print(list+[7,9,0])
print([1,2,3]+[4,5,8])
#list membership test:"in" and "not in"
li=[1,2,3,"1","hi",0,"hello"]
print(1 in li)
print("1" in li)
print("hello" in li)
print(1 and 2 and 3 in li)
print(1 or 7 not in li)
#nested list
st=["python",[1,2,3],["a"]]
print(st)
print(st[0])
print(st[2])
# print(st[3]) index error
print(st[1][2])
# print(st[2][1])index error
print(st[0][2])
#list constructor:list(())
# myl=list(('myphone','mobikle','types'))
# print(myl)
#list are mutable
mylist=["usa","india","china"]
print(mylist)
mylist[2]="pakistan"
print(mylist)
mylist.append("germany")
mylist.extend("Bhopal")

print(mylist)
#count
st=[1,2,3,1,1,"1",2,"2"]
print(st.count(1))
#clear()
st.clear()
print(st)
# del st# st is not definned
k=[1,2,3]
# del k
# print(k)
#append(),extend(),insert(),copy(),list(),max(),min(),sort(),count(),index()
#practice questions
#find length of list
#find elements to list
#indexing,slicing
#join two list
#list methods
#copy lists elements

