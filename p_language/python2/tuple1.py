#tuple is sequence/collection which is ordered/indexed.
#tuple is immutable.
#written using()
tpl=()
print(tpl)
print(type(tpl))
tpl=(40,)
print(tpl)
print(type(tpl))
tpl=(10,20,30,40,50,90)
print(tpl)
#indexing
print(tpl[0])
print(tpl[3:2])
print(tpl[-3:-2])
print(tpl[-2:-3])
print(tpl[3:])
#repetition
a=tpl*3
print(a)
# print(tpl[8.0])type error
#change tuple values
a=("python","django","tilu")
print(a)
a=list(a)
print(a)
a[2]="summit"
print(a)
print(type(a))
print(tuple(a))
#nested tuple
a=("python","django",("kkin s",12))
print(a)
print(a[0])
print(a[2])
print(a[2][1])
b=("python","kk",["dhdhd0","hu"])
print(b)
print(b[2])
b[2][1]="kumar"
print(b)
c=["kumar","shristi",("trupti","gayatri")]
print(c)
# [print(c[2][1])]
# c[2][1]="bishal"
print(c)
for i in range(len(c)):
    if c[i] in  c:
        print(c[i])
        c[i]=list(c[i])
        print(c[i])
        c[i][1]="khusi"
        print(c[i])
#membership in and not in
l=("h","e","l","l","o")
print(l)
print("o" in l)
print("h" not in l)
print("h in l")
#tuple constructor
k=tuple(("bishal","shirsiti","hhsh"))
print(k)
m=["11",1,2,3]
#index
print(m.index("11"))
del m[1]
print(m)
n=(1,2,3,4)
print(n.index(3))
# del n(2)syntax error
# del n[2]type error
del n
#tuple concatenations
a=(1,2,3,4)
b=(5,"11",2,3,4,1)
print(a+b)
print(a+(3,))
print((9,9,1)+(88,11,))
#adding items to tuples
print(b)
k=list(b)
print(k)
k.append("bishal")
print(k)
k.extend("bishal")
print(k)
print(tuple(k))
t=(1,2,3,4,4,9,2)
print(t[::-1])
#tuple methods:count(),index()
#create a tuple
#indecing and slicing,reverse the tuple
#adding elements to tuple
#nested tuples
#membership opearators
#tuple concatenations
#tuple constructors
