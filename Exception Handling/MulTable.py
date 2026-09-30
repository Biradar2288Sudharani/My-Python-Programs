# MulTable.py----File Name and Module Name
from MulExcept import NagativeNumberError, ZeroError
def multable(n):
    if(n==0):
        raise ZeroError
    elif(n<0):
        raise NagativeNumberError
    elif(n>0):
        print("*"*50)
        print("Mul Table For {}".format(n))
        print("*"*50)
        for i in range(1,11):
            print("\t\t {}X{}={}".format(n,i,n*i))    
        print("*"*50)   










