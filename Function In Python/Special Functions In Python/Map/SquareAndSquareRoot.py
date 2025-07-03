# WAPP which will accept list of numerical values and optaining their square and square roots. 
# SquareAndSquareRoot.py
# Logic 1
def square(value):
    return (value**2)
def squareroot(value):
    return (value**0.5)
# Main Program
print("Enter list of numbers:")
lst=[float(val) for val in input().split()]
obj=map(square,lst)   # map concept---here obj is an object class of map.
obj1=map(squareroot,lst)  # map concept---here obj1 is an object class of map.
# Convert map object into list type.
sqlist=list(obj)
sqrtlist=list(obj1)
print("*"*70)
print("Given Number\t Square \t\t Square Root")
print("*"*70)
for n, sqr,sqrt in zip(lst,sqlist,sqrtlist):
    print("{} \t\t Square({})={} \t Square Root({})={}".format(n,n,round(sqr,2),n,round(sqrt,2)))
print("*"*70)  


# Logic 2
def square(value):
    return (value**2)
def squareroot(value):
    return (value**0.5)
# Main Program
print("Enter list of numbers:")
lst=[float(val) for val in input().split()]
# Convert map object into list type.
sqlist=list(map(lambda value:value**2,lst))
sqrtlist=list(map(lambda value:value**0.5,lst))
print("*"*70)
print("Given Number\t Square \t\t Square Root")
print("*"*70)
for n, sqr,sqrt in zip(lst,sqlist,sqrtlist):
    print("{} \t\t Square({})={} \t Square Root({})={}".format(n,n,round(sqr,2),n,round(sqrt,2)))
print("*"*70)


''' --> ANSWER <--
Enter list of numbers:
4 64 49 33 81 50 83
**********************************************************************
Given Number     Square                  Square Root
**********************************************************************
4.0              Square(4.0)=16.0        Square Root(4.0)=2.0
64.0             Square(64.0)=4096.0     Square Root(64.0)=8.0
49.0             Square(49.0)=2401.0     Square Root(49.0)=7.0
33.0             Square(33.0)=1089.0     Square Root(33.0)=5.74
81.0             Square(81.0)=6561.0     Square Root(81.0)=9.0
50.0             Square(50.0)=2500.0     Square Root(50.0)=7.07
83.0             Square(83.0)=6889.0     Square Root(83.0)=9.11
**********************************************************************
'''























