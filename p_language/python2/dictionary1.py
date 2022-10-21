#Dictionary is a collection which is ordered/unindexed.
#it is a key value pairs
#written using{}
dict1={}
print(dict)
print(type(dict1))
d={1:"bishal",2:"shristi",3:"kumari"}
print(d)
d={1:"bishal",
    2:"kumari",
    3:'trupti'}
print(d)

#Accessing items on dictionary
print(d[1])
print(d[2])
#length of dictionary
print(len(d))
#Change value of an item
d[2]="Sumit"
print(d)
#adding an elment to dictionary
d["color"]="grey"
print(d)
#loop through acces keys
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)
for i,j in d.items():
    print(i,j)
#remove dictionary
d.pop(3)
print(d)
d.popitem()
print(d.popitem())
#nested dictionary
d1={1:"abhi",2:"2",3:"3","color":{4:["dictionary","shirtis"]}}
print(d1)
print(d1["color"][4][1])
# dictionary constructor
a=dict(abhi=123,sumit=12333,dbdbbd=1122)
print(a)
# practice questions
# create a dictionary
# access items to dictionary
#add items to dictionary
#change value of dictionary
# nested dictionary
# dict constructor:dict()