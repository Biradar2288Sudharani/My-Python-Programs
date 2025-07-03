a=[10,20,30,40]
print(a,type(a))
b=bytearray(a)
print(b,type(b))

'''
a=[-10,20,30,40]
print(a,type(a))
b=bytearray(a)
print(b,type(b))

a=[10,20,30,40,256]
print(a,type(a))
b=bytearray(a)
print(b,type(b))

'''

a=[10,20,30,40,255]
print(a,type(a))
b=bytearray(a)
print(b,type(b))
for i in b:
    print(i)
print(b[0])
print(b[-1])
for i in b:
    print(i)
for i in b[::-1]:
    print(i)
print(b[0:5])
for i in b[0:5]:
    print(i)


