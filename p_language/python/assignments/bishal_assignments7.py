'''1.Demonstrate the following functions for dictionaries:
   d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
  1.copy
  2.dictionary constructor
  3.length of dictionary
  4.remove item from the dictionary
  5.delete dictionary'''
  
'''2.using keys and indexing,print 'python; from the dictionaries:

d1={'key':'python'}
d2={'key1':{'key2':'python'}}
d3={'key1' : [{'nest_key':["let's learn",['python']]}]}'''

'''3.Given the dictionary change empid to "AA22"
thisdict = {
  "emp_name": "Rahul",
  "emp_id": "AA11",
  "emp_salary": 10000
}  
'''
#4.Refering dictionary in question 3 add an item to this dict dictionary, and also delete the same item added to the dictionary.
# 1.Ans
d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
d2=d1.copy()
print(d2)
print(type(d2))
dict1=dict(nam="john",age="30",city="dubai",country="UAE")
print(dict1)
print(len(dict1))
dict1.pop("nam")
print(dict1)
del dict1
# print(dict1)
# 2.Ans
d1={'key':'python'}
d2={'key1':{'key2':'python'}}
d3={'key1' : [{'nest_key':["let's learn",['python']]}]}
print(d1['key'])
print(d2['key1']['key2'])
print(d3['key1'][0]["nest_key"][1][0])
# 3.Ans
thisdict = {
  "emp_name": "Rahul",
  "emp_id": "AA11",
  "emp_salary": 10000
}  
thisdict["emp_id"]="AA22"
print(thisdict)
thisdict["emp_age"]=35
print(thisdict)
thisdict.popitem()
print(thisdict)

