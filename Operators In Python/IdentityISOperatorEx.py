# IdentityISOperatorEx.py

# Example 1
a="PYTHON"
print(a,type(a),id(a))
b=a    # Deep Copy
print(b,type(b),id(b))
print(a is b)

# Example 2
a=[10,"rs"]
b=a.copy()
print(a,type(a))
print(b,type(b))
print(a is b)

# Example 3
a=None
b=None
print(a is b)

# Example 4
a={10:"apple",20:"mango"}
a={10:"apple",20:"mango"}
print(a is b)

# Example 5
a={10,20,30,40}
a={10,20,30,40}
print(a is b)

# Example 6
a={10,20,30,40}
b=frozenset(a)
c=frozenset(b)
print(b is c)

# Example 7
a=[10,"sudha","bang"]
b=[10,"sudha","bang"]
print(a is  b)

# Example 8
a=range(10,20,2)
b=range(10,20,2)
print(a is b)

# Example 9
a=bytearray([10,20,30,40])
b=bytearray([10,20,30,40])
print(a is b)

# Example 10
a=bytes([10,20,30,40])
b=bytes([10,20,30,40])
print(a is  b)

# Example 11
a="INDIA"
b="INDIA"
print(a is b)
a="india"
b="india"
print(a is  b)

# Example 12
a=2+3j
b=2+3j
print(a is  b)

# Example 13
a=True
b=False
print(a is  b)
b=True
a=False
print(a is  b)

# Example 13
a=1.2
b=1.2
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 14
a=300
b=300
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 15
a=100
b=100
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 16
a=256
b=256
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 17
a=257
b=257
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 18
a=-1
b=-1
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 19
a,b=1.2,1.2
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 20
a,b=300,300
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 21
a,b=20,10
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 22
a,b=2+3j,2+3j
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 23
a,b=[10,"KVR"],[10,"KVR"]
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 23
a,b={10:"apple"},{10:"apple"}
print(a, id(a))
print(b, id(b))
print(a is  b)

# Example 23
a,b=[10,"KVR"],[10,"KVR"]
print(a, id(a))
print(b, id(b))
print(a is  b)








