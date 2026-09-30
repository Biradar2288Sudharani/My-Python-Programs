# BitwiseXOROperatorEx.py
print(0^1)
print(1^0)
print(0^0)
print(1^1)

print(True^True)
print(False^False)
print(True^False)
print(False^True)

# print("apple"^"mango")-->TypeError: unsupported operand type(s) for ^: 'str' and 'str'
# print("1.2"^"3.4")-->TypeError: unsupported operand type(s) for ^: 'str' and 'str'

a={10,20,30}
b={30,40,50}
c=a.symmetric_difference(b)
print(c)

a={10,20,30}
b={30,40,50}
c=a^b
print(c)

a={1.0,2.0,3.0}
b={3.0,4.0,5.0}
c=a^b
print(c,type(c))

a={1.0,2.0,3.0}
b={3.0,4.0,5.0}
c=(a|b)-(a&b)
print(c,type(c))

a=3
b=2
c=a^b
print(c)

print(10^15)
print(3^4)

''' Answers
1
1
0
0
False
False
True
True
{40, 10, 50, 20}
{40, 10, 50, 20}
{1.0, 2.0, 4.0, 5.0} <class 'set'>
{1.0, 2.0, 4.0, 5.0} <class 'set'>
1
5
7
'''
# WAPP which will accept any two integer values & swap them, by using Bitwise XOR
# Logic 1
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
print("\t Original value of a={}".format(a))
print("\t Original value of b={}".format(b))
a=a^b
b=a^b
a=a^b
print("\t Swaped value of a={}".format(a))
print("\t Swaped value of b={}".format(b))

# Logic 2
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
print("\t Original value of a={}".format(a))
print("\t Original value of b={}".format(b))
t=a
a=b
b=t
print("\t Swaped value of a={}".format(a))
print("\t Swaped value of b={}".format(b))

# Logic 3
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
print("\t Original value of a={}".format(a))
print("\t Original value of b={}".format(b))
a=a+b
b=a-b
a=a-b
print("\t Swaped value of a={}".format(a))
print("\t Swaped value of b={}".format(b))


