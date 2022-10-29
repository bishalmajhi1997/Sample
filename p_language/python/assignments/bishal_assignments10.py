#1.Write python program to find the largest of three numbers.
#2.Write a python program to check whether a person can get a driving license (consider age to be 18 and above)
#3.Write a program to check student result for below marks and display grade
#   '''90 or above is equivalent to an A grade
#   80-89 is equivalent to a B grade
#   70-79 is equivalent to a C grade
#   65-69 is equivalent to a D grade
#   64 or below is equivalent to an F grade'''
# 1.Ans:
a=int(input("Enter your First numbers:"))
b=int(input("Enter your second numbers:"))
c=int(input("Enter your third numbers:"))
if(a>b and a>c):
    print(a," is greater than b and c.")
elif(b>a and b>c):
    print(b," is greater than a and c.")
else:
    print(c," is greater than a and b.")
# 2.Ans:
person_age=int(input("Enter Age:"))
if (person_age>18):
    print("Person can get a driving license.")
else:
    print("Person can not get a driving license.")
# 3.Ans:
student_marks=int(input("Enter your student marks:"))
if(student_marks>=90):
    print("Grade A")
elif(student_marks>=80 and student_marks<=89):
    print("Grade B")
elif(student_marks>=70 and student_marks<=79):
    print("Grade C")
elif(student_marks>=65 and student_marks<=69):
    print("Grade D")
else:
    print("Grade F")
