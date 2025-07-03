a=3.14
print(a,type(a))  # 3.14 <class 'float'>
a=3.23
b=3.87
c=a+b
print(c,type(c))  # 7.1 <class 'float'>
a=3e2
print(a)  # 300.0
a=2E2
print(a)  # 200.0
a=3e-2
print(a)  # 0.03
a=2^3
print(a)  # 1
a=0.0000000000000000000000000000000000000000000000000005
print(a)  # 5e-52

'''
a=0b0001.0b0000
print(a)  #  SyntaxError:invalid decimal literal
a=0o123.0b11010
print(a)  #  SyntaxError:invalid decimal literal
a=0xBEE.0xFace
print(a)  #  SyntaxError:invalid decimal literal
'''