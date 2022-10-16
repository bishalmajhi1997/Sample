'''1.Given the tuples:
   t1=("hi",1,2,5)
   t2=(6,7,8)
   Concatenate the tuples.'''
   
#2.Create tuples using constructors.  

'''3.change the tuple item from 'tulip' to 'lotus' in  below tuple using suitable method
  tp=('rose','lily','tulip','jasmine')


#4.Demonstrate working of copy function for tuples.'''


'''5.Given tuple:
  tuple=['c','o','o','l')
  demonstrate membership test.'''
# 1.Ans:
from colorama import AnsiToWin32


t1=("hi",1,2,5)
t2=(6,7,8)
print(t1+t2)
#2.Ans
t1=tuple(("bishal","kumar","10.00",11,True))
print(t1)
#3.Ans:
tp=('rose','lily','tulip','jasmine')
tp=list(tp)
tp[2]="lotus"
print(tuple(tp))
#4.Ans:
tp=("abhi","suresh",10,True)
tp=list(tp)
tp1=tp.copy()
print(tuple(tp1))
#5.Ans:
tuple=('c','o','o','l')
print("o" in tuple)
print("o" not in tuple)
# output:
# 1.('hi', 1, 2, 5, 6, 7, 8)
# 2.('bishal', 'kumar', '10.00', 11, True)
# 3.('rose', 'lily', 'lotus', 'jasmine')
# 4.('abhi', 'suresh', 10, True)
# 5.True
# 5.False



