# BitwiseOROperatorEx.py

print(0|1)
print(1|0)
print(0|0)
print(1|1)

a=10
b=5
c=a | b
print(c)
a=10
b=10
c=a | b
print(c)

print(10|5)
print(10 or 5)
print(5 or 10)
print(5|10)

a={10,20,30}
b={20,25,35}
c=a.union(b)
print(c,type(c))

a={10,20,30}
b={20,25,35}
c=a|b
print(c,type(c))

a={"apple","mango"}
b={"kiwi","mango"}
c=a|b
print(c,type(c))

a={"apple"or "mango"}
b={"kiwi"or "mango"}
c=a|b
print(c,type(c))

# print("apple"|"mango") -->TypeError: unsupported operand type(s) for |: 'str' and 'str'

a={1.2,2.5,3.6}
b={7.3,2.5,3.5}
c=a|b
print(c,type(c))

#print(1.2|1.3) -->TypeError: unsupported operand type(s) for |: 'float' and 'float'

print(1.2 or 1.3)

'''
1
1 
0 
1 
15
10
15
10
5 
15
{35, 20, 25, 10, 30} <class 'set'>
{35, 20, 25, 10, 30} <class 'set'>
{'mango', 'apple', 'kiwi'} <class 'set'>
{'apple', 'kiwi'} <class 'set'>
{1.2, 2.5, 3.6, 3.5, 7.3} <class 'set'>
1.2
'''