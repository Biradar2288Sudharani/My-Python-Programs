a=[10,20,30]
print(a,type(a))

a=[10,20,30,255]
print(a,type(a))
b=bytes(a)
print(b,type(b))

'''
a=[10,20,30,256]
print(a,type(a))
b=bytes(a)
print(b,type(b))


a=[-10,20,30,255]
print(a,type(a))
b=bytes(a)
print(b,type(b))
'''
for i in a:
    print(i)
'''
for i in a:  ......Indentation Error
print(i)
'''

a=[10,20,30,40,50]   # all bytes object we can perform both indexing and slicing operation.
print(a,type(a))
b=bytes(a)
print(b,type(b))
print(b[0])
print(b[0:3])
for i in b[0:3]:
    print(i)


a=[10,20,30,255]   # an objects of bytes belongs to immutable because
print(a,type(a))   # 'bytes' object does not support item assignment'
b=bytes(a)
print(b,type(b))
print(b[0])
b[0]=100
    




    
