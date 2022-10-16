#1.convert a string to floating point number and also check the datatype.
#2.convert a  floating point number to integer and also check the datatype.
#3.give the binary,hexadecimal and octal representation of 20.
#1.Ans:
a="10"
b=float(a)
print(b)
print(type(b))
# 2.Ans:
a=10.99
b=int(a)
print(b)
print(type(b))
# 3.Ans:
a=20
print(bin(a))
print(oct(a))
print(hex(a))
# output
# 1.10.0
# 1.<class 'float'>
# 2.10
# 2.<class 'int'>
# 3.0b10100
# 3.0o24
# 3.0x14
