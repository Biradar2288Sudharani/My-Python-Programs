# BitwiseANDOperatorEx.py

print(0&1)
print(1&0)
print(1&1)
print(0&0)

a=10
b=40
c=a&b
print(c,type(c))
                                     
print(4&3)
print( 4 or 3 )
print(3 and 4)
print(10 & 15)
print(30 & 20)
print(20 and 30)
print(30 and 20)

# Important Questions for Bitwise AND Operator
a={10,20,30}
b={20,25,35}
c=a.intersection(b)
print(c,type(c))

a={10,20,30}
b={20,25,35}
c=a&b
print(c,type(c))

a={"apple","mango"}
b={"kiwi","mango"}
c=a&b
print(c,type(c))

'''
a={1.2,3.4}
b={4.2,5.2} --> TypeError: unsupported operand type(s) for &: 'float' and 'float'
c=a&b
print(c,type(c))
''' 

print("apple", "mango") 

# print(1.2 & 3.4) --> TypeError: unsupported operand type(s) for &: 'float' and 'float'

print(1.2 and 3.4)

''' Answers
0
0
1
0
8 <class 'int'>
0
4
4
10
20
30
20
{20} <class 'set'>
{20} <class 'set'>
{'mango'} <class 'set'>
apple mango
3.4
'''















