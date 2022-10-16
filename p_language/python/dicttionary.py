#Dictonary is a collection which is ordered and unindexed.
# it is a key value pairs.
#Written using {}
dict1={}
print(dict1)
print(type(dict1))

d={1:"john",2:"abhi",3:"suresh"}
print(d)
mydict={
    "brand":"bmw",
    "models":"3series",
    "year":2019
}
print(mydict)
#Accessing items on dictionary
print(mydict["brand"])
print(mydict["year"])

#length of dictionary
print(len(mydict))

#change your value of an item
#change year to 2018
mydict["year"]=2018
print(mydict)

#adding an element to dictionary.
mydict["color"]="black"
print(mydict)

#loop through 
# the access keys
k=mydict.keys()

for i in k:
    print(i)
t=mydict.values()

for i in mydict.values():print(i)

for i in t:
    print(i)

for i in mydict:
    print(i) 

for i in mydict.items():
    print(i)

#loop through both keys and values
for i,j in mydict.items():
      print(i,":",j)
      print(i,j,sep=":")

#remove dictionary items -pop(),popitem()
mydict.pop('models')
print(mydict)

mydict.popitem()
print(mydict)
mydict.pop("year")
print(mydict)
mydict.popitem()
print(mydict)

#Nested dictionary
d1={"key1":"123","key2":"value2","key3":{"inside":[1,2,"hello"]}}
print(d1)
print(d1["key1"])
print(d1["key2"])
print(d1["key3"])
print(d1["key3"]["inside"][2])
print(d1["key3"]["inside"][2][4].upper())
print(d1["key3"])


#dictionary constructor-dict()

#practice questions
#create a dictionary
#access items to dictionary
#add items to dictionary
#change value of a dictionary
#nested dictionary
#dict constructor