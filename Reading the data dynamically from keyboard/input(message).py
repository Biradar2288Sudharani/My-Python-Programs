# input(message)
'''
a=input("enter the any value")
print("value of a:",a)
print("type of a:",type(a))

# WAPP which will accept two numerical value and compute their addition
a=input("enter first value")
b=input("enter second value")
c=a+b
print(c)

a=input("enter first value")
b=input("enter second value")
x=float(a)
y=float(b)
z=x+y
print("first value {}" .format(x))
print("second value {}" .format(y))
print("sum={}" .format(z))

a=float(input("enter first value"))
b=float(input("enter second value"))
c=a+b
print("first value {}" .format(a))
print("second value {}" .format(b))
print("sum={}" .format(c))

c=float(input("enter first value"))+float(input("enter second value"))
print("first value {}" .format(a))
print("second value {}" .format(b))
print("sum={}" .format(c))

print("enter two values")
a=float(input())
b=float(input())
print("first value: {}" .format(a))
print("second value: {}" .format(b))
print("sum({},{})={}" .format(a,b,a+b))

print("enter two values")
print("sum={}" .format(float(input())+float(input())))

print("sum={}" .format(float(input("enter first value:"))+float(input("enter second value:"))) )

# WAPP which will calculate area of rectangle
length=float(input("enter length"))
breadth=float(input("enter breadth"))
area=length*breadth
print("length = {}" .format( length))
print("breadth = {}" .format( breadth))
print("area = {}" .format( area))

# WAPP which will calculate perimeter or circumferance of rectangle
length=float(input("enter length"))
breadth=float(input("enter breadth"))
perimeter=(2*length*breadth)
print("length = {}" .format( length))
print("breadth = {}" .format( breadth))
print("perimeter = {}" .format(perimeter))

# WAPP which will calculate area of circle
radius=float(input("enter radius"))
area=3.142*radius*radius
print("radius = {}" .format(radius))
print("area = {}" .format(area))

# WAPP which will calculate area & perimeter
side=float(input("enter side"))
area=side*side
perimeter=4*side
print("area = {}" .format(area))
print("perimeter = {}" .format(perimeter))
'''
# SPECIAL POINTS
s="Sudha"
s=s+s+s
print(s)

a=[10,"ma"]
print(a*5)

a="Sudha"
a=3*a
print(a)

print(2*5)

a="="
a=a*50
print(a)

print("*",60)

print("#",70)

print("ma"+"ma")

# print("ma"*"ma")-->TypeError: can't multiply sequence by non-int of type 'str'

print("ma"*4)

print("hyd"*4*2)

# print("hyd"*4+2)-->TypeError: can only concatenate str (not "int") to str

print(str(2)+"pyt"*2)

print((str(2)+"pyt")*2)

print("+"*(len("sudha")+2))