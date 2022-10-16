#1.Create a string, display it and check its data type
'''2.Given the string :
      #s = "django"
Use indexing to print out the following:
‘d’ , ‘o’ , ’jan’ ,’djan’,’go’.
And Also reverse the above string.'''

'''3.Demonstrate following string methods on gvien string.
    S = '  Python is easy   '
    remove white spaces of string from both ends
	show the occurences of character in string
	locate a substring.'''
#1. Ans:
from audioop import reverse


a="Website"
print(a)
print(type(a))
# 2.Ans:
s="django"
print(s[0])
print(s[-1])
print(s[1:4])
print(s[:-2])
print(s[4:])
print(s[::-1])
# 3.Ans:
S="   Python is easy   "
print(S.strip())
print(S.count("y"))
print(S.find("is"))
# output
# 1.Website
# 1.<class 'str'>
# 2.d
# 2.o
# 2.jan
# 2.djan
# 2.go
# 2.ognajd
# 3.Python is easy
# 3.2
# 3.10
