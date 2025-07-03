# aop.py
def sumop(a,b):
    print("Sum({},{})={}".format(a,b,a+b))
def subop(a,b):
    print("Sub({},{})={}".format(a,b,a+b))
def mulop(a,b):
    print("Mul({},{})={}".format(a,b,a*b))
# Main Program
sumop(10,20)
subop(10,20)
mulop(10,20)
print("*"*50)