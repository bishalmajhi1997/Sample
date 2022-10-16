#Tuple is sequence/collection which is ordered and indexed.
#Tuples are immutable.
#written using ()


tpl=()
print(tpl)
print(type(tpl))
tpl=(40,)
print(tpl)
print(type(tpl))
tpl=(40,50,60,90,"xyz")
print(tpl)
#indexing
print(tpl[0])
# print(tpl[8]) out of index
# print(tpl[2.0]) error
#slicings
print(tpl[0:1])
print(tpl[4:])
print(tpl[-2:-1])
print(tpl[-1:-2])
#repetition
print(tpl*3)
#length of tuple
print(len(tpl))
#we can not perform methods sucg insert(),append(),extend(),clear(),remove()
#change tuple values
x=("python","django","html")
# x[2]="js"
# print(x)#type error
y=list(x)
print(y)
y[2]="js"
print(y)
z=tuple(y)
print(z)
#nested tuples
tpl1=("hello",(1,2,3),("xyz"),"z")
print(tpl1)
print(tpl1[0])
print(tpl1[2][2])
# print(tpl1[3][1])index error
print(tpl1[1][0])
#membership "in" and "not in"
a=("h","e","l","l","o")
print("o" in a)
# print("o" not in tuple)#type error
print("o in a")
#tuple constrctor:tuple(())
my_tpl=tuple(("rose","abhi","shristi","gayatri"))
print(my_tpl)
#tuple methods
#index
t1=(1,2,3,4,5,67,8,9,0)
# print(t1.index(11)) value error
print(t1.index(67))
#count
print(t1.count(2))
# del t1[3]#we can not delete tuple elements
print(t1)
del t1 #we can delete whole tuple.
# print(t1)#name error
#tuple concatenation
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)
print(t1+(3,4,5))
print((9,9,1)+(8,1,1))
#adding items to tuples
tpl=("ajit","moulali")
tpl=list(tpl)
tpl.append("10000")
print(tpl)
tpl=tuple(tpl)
print(tpl)
#tuple methods:count(),index()
#practice questions
#create a tuple
#indexing and slicing,reverse the tuple
#tuple methods
#adding elements to tuples
#Nested Tuples
#Memeberships opearators
#tuple concatenations
#tuple constructors