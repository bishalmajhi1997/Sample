#1.using suitable control statement ,print item i as long as i is less than 8.
#2.Write a Python  program to find the product of numbers in a list.
#3.Display numbers from 1 to 30 using looping statements.
#4.Write a Python program to count the number of even and odd numbers from a series of numbers.
'''5.Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Foo" instead of the number and for the multiples of five print "Bar".
For numbers which are multiples of both three and five print "FooBar".'''
#1. Ans
# using for loop
for i in range(0,7):
    print("i")
# using while loop
print()
k=0
while(k<8):
    k+=1
    print("i")
# 2.Ans
k=[1,2,3,4,88]
product=1
for i in range(0,len(k)):
    product*=k[i]
print(product)
# 3.Ans
# using for loop
for i in range(0,31):
    print(i)

# 4.Ans
even_count=0
odd_count=0
for i in range(0,30):
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Series of odd number is",odd_count)
print("Series of even_numbers is",even_count)
# 5.
for i in range(1,51):
    if(i%3==0):
        print("Foo")
    elif(i%5==0):
        print("Bar")
    if((i%5==0) and (i%3==0)):
        print("FooBar")
    