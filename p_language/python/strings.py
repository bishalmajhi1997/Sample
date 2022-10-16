#sequences
#strings
#strings are sequences of charecters enclosed within single and double codes.
print("hi")
print("hi")
#Assing string to a variable.
s="python is easy"
print(s)
#indexing
s="python is easy"
print(s[0])
print(s[4])
print(s[6])
print(s[4])
print(s[-2])#negative indexing
print(s[-4])
# print(s[-15])#indexerror
#slicing:
print(s[0:6])
print(s[0:9])
print(s[4:10])
print(s[-3:-1])
print(s[-2:-3])
#step value to slices
print(s[0:9])
print(s[0:9:2])#2 is stop value
print(s[0:9:3])
print(s[::-1])#reverse the string
print(s[:9])
print(s[0:])
#string methods
#strip()
s="    you are awesome   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
#find-locate substring in given string
print(s.find("are"))
#count:return the number of occurances of specific elements.
print(s.count('e'))
print(s.count("a"))
#Replace
print(s.replace("awesome","cool"))
print(s)
k=s.replace("awesome","nice")
print(k)
#upper(),lower(),title()
print(s.upper())
print(s.lower())
print(s.title())
#split:splits the substring if it findes the instances of separators
a="Hello,world"
print(a.split(","))
b="he lloworld"
print(b.split(" "))
print(s.isdigit())
print(s.startswith("y"))
print(s.endswith(" "))
print(s.swapcase())
#check string :"in and not in"
txt="No gain without pain"
print("ain" in txt)
print("out in text")
print('out' in txt)
print("msnns" not in txt)
print("out" not in txt)
#string concatenation :joining/combining
a="Hello"
b="World"
print(a+b)
print(a+" "+b)
c=a+" "+b
print(c)
#length of string
print(len(c))
# x="hello"+100 #error
s="Hello"+str(100)
print(s)
age=10
marks=93.5
text="My NAME IS JOHN AND i am {},marks  are {}"
print(text.format(age,marks))
#strings are immutable
s1="python"
print(s1)
# s1[1]="a"
# print(s1)#type error
# del s1[1]#type error
# del s1
# print(s1)#name error
mystr="levelup"#python deoes not have char data type,one single charecter is string.
print(mystr)
print(len(mystr))

mystr="l"
print(mystr)
print(len(mystr))
#repitition of string
s="levelup"
print(s*3)
print((s+" ")*3)