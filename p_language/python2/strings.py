#Strings are sequences of charecters enclosed within single quotation and double quotaions.
print('Hi')
#Assign String to variable.
a="Python is easy."
print(a)
#indexing
s="Python is easy"
print(s[0])
print(s[1])
print(s[6])
print(s[-2])
print(s[-3])
#slicing
a="Python is easy"
print(s[0:6])
print(s[0:9])
print(s[4:10])
print(s[-7:-2])
print(s[-1:-3])
#step value to slices
print(s[0:9])
print(s[0:6:2])#2 is step value
print(s[0:9:3])
print(s[:9])
print(s[0:])
#string methods.
#1.strip
k="  You are good boy  "
print(k.strip())
print(k.lstrip())
print(k.rstrip())
#2.locate a substring in a given string.
print(k.find("are"))
print(k.find("ou"))
#3.count
print(s.count("e"))
print(k.count("o"))
#4.replace
print(k.replace("good","bad"))
print(k)
#5.upper(),title(),lower()
print(k.upper())
print(k.lower())
print(k.title())
#6.split.it spilts the substring if it finds instance of separator.
k="My name is bishal, i am coming from hyderbad."
k=k.split(", ")
print(k)
k="my name is bishal# i am coming from bangalore"
m=k.split('# ')
print(m)
k="my name is dbhd, msmsmmsm, ssjs,sjsjjs"
n=k.split(",",2)
print(n)
n="hell  oeooe"
print(n.split( ))
print(n.isdigit())
n="10"
print(n.isdigit())
print(k.startswith("m"))
print(k.endswith('s'))
print(k.swapcase())
m="Sumit is good girl."
print(m.swapcase())
#Check string 'in' and 'not in'.
print('sumit' in m)
print('umit' in m)
print('sumit' not in m)
print('mit' not in m)
# print(mit not in m) nameerror
#string concatenation joining/combining
a="hello"
b="bevit"
print(a+" "+b)
print("hello"+str(100))
#using format method
age=10
marks=95.5
print("my age is {} and my marks is {}".format(age,marks))
#Python does not have char data types,one single charecter is simply string of length 1.
print(len("kumar"))
print(len("m"))
print(k*3)
print("k*3")
print((k+" hh ")*3)
m="bishal"
n=list(m)
print(n)
a="split"
b=list((a))
print(b)