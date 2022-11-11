#Naming a module:we can name the module file,whatever we want  but it must have .py extensions files.
# Renaming:we can rename a module by creating an alias name while importing
# module by using "as" keyword
import calc as cl
x=cl.person["name"]
print(x)
# import from module
# we can choose to import only parts from a module by using form keyword. 
from calc import person
print(person["age"])
from calc import add
print(add(3,4))
from calc import mul
print(mul(4,7))