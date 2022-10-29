# functions arguments/parameters
def func(a):
    x=10
    print("x is:",x)
func(5)

def update(lst):
    print(id(lst))
    lst[2]=30
    print(id(lst))
    print("list is:",lst)
# lst=[10,15,20]
# update(lst)
update([10,20,40])
# update((10,20,40)) type error
def upt(tpl):
    x=list(tpl)
    x[2]=55
    y=tuple(x)
    print("tuple is:",y)
upt((10,20,40))
x=[10,30]
x.append(3)
print(x)