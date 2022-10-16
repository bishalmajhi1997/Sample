'''1. Given the nested list:
   l=[2,3,[1,6,'Java']]
   Reassign 'Java' to 'Python'.'''
   
#2.Demonstrate working of copy function for list.  

'''3.Join the below two lists
  l1=[1,2,3]
  l2=[4,5,6]'''
   
#4.Create list using constructor. 
 
'''5.Given list:
  lst=['w','e','l','c','o','m','e']
  demonstrate list membership test.'''


'''6.Given the list
  l1=[1,2,3,'abc',4,5,6]
 perform indexing to print 'abc'
 perform slicing to print 4,5
 perform negative indexing
 add an element to list
 add an element specific position in list
 remove an element of list
 pop specific element of list'''
#1.Ans:
l=[2,3,[1,6,'Java']]
l[2][2]="Python"
print(l)
#2.Ans:
l=[2,3,[1,6,'Java']]
k=l.copy()
print(l)
print(k)
# 3.Ans:
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
# 4.Ans:
li=list(("string","constructor","media",12,True,12.99))
print(li)
# 5.Ans:
lst=['w','e','l','c','o','m','e']
print("w" in lst)
print("w" not in lst)
# 6.Ans
l1=[1,2,3,'abc',4,5,6]
print(l1[3])
print(l1[-3:-1])
print(l1)
print(li[-2:])
l1.append("bishal")
print(l1)
l1.extend("bishal")
print(li)
l1.insert(2,"waited")
print(l1)
l1.remove("abc")
print(l1)
l1.pop(2)
print(l1)
#output
#1. [2, 3, [1, 6, 'Python']]
#2.[2, 3, [1, 6, 'Java']]
#2. [2, 3, [1, 6, 'Java']]
#3.[1, 2, 3, 4, 5, 6]
#4. ['string', 'constructor', 'media', 12, True, 12.99]
#5.True
#5. False
#6. abc
#6. [4, 5]
#6. [1, 2, 3, 'abc', 4, 5, 6]
#6. [True, 12.99]
#6. [1, 2, 3, 'abc', 4, 5, 6, 'bishal']
#6. ['string', 'constructor', 'media', 12, True, 12.99]
#6. [1, 2, 'waited', 3, 'abc', 4, 5, 6, 'bishal', 'b', 'i', 's', 'h', 'a', 'l']
#6. [1, 2, 'waited', 3, 4, 5, 6, 'bishal', 'b', 'i', 's', 'h', 'a', 'l']
#6. [1, 2, 3, 4, 5, 6, 'bishal', 'b', 'i', 's', 'h', 'a', 'l']






