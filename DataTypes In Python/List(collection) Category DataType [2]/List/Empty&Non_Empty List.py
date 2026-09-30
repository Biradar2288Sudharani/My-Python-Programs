# EMPTY AND NON EMPTY LIST
a=[1,2,3,4,-1]
print(a,type(a))

b=[10,"sudha",3.14,True]
print(b,type(b))
print(a[0])
print(b[3])
print(a[0:2])

b=[10,"sudha",3.14,True,3+4j]
print(b,type(b),id(b))
b[1]="sudharani"
print(b,type(b),id(b))
b[0]=[3,"rani"]
print(b,type(b),id(b))

# list having two types

# empty list
a=" "
print(a,type(a),id(a))
print(len(a))

a=[]
print(a,type(a))
print(len(a))
a=list()
print(a,type(a))

a=list()
print(a,type(a))
print(len(a))

# non-empty list
# SYNTAX - 1 : varname[val1,val2,.........,val-n]
a=[10,"sudha",True]
print(a,type(a),id(a),len(a))

# SYNTAX - 2 : varname
a="sudha"
print(a,type(a))
b=list(a)
print(b,type(b))

a=[10,20,30,255]
print(a,type(a))
b=bytes(a)
c=list(b)
print(c,type(c))
