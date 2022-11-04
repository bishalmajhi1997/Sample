#Logical operators are used to combine conditional statements
#'and','or' and 'not'
'''
x and y - True if both are true
x or y  - True if either x or y is true
not -  changes to opp(T-F,F-T)
'''

x=20
y=30
print(x==20 and y==31)
print(x==20 and y==30)
print(x>=25 or y==31)
print(x<25 or y==31)
print(not(x==20 and y!=30))