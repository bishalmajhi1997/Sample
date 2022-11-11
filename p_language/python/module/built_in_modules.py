# Built in modules...
import platform
z=platform.system()
print(z)
# Program to calculate area of circle.
import math
r=float(input("enter radius"))
area=math.pi*r**2
print("area of circle is:",area)
# import all names
from math import *
print(pi)
print(factorial(6))
print(sqrt(25))

# dir()
import math
print(dir(math))
from math import pi
print(pi)
# random module()
import random
print(random.randint(0,5))
print(random.random())#o to 1
print(random.random()*200)