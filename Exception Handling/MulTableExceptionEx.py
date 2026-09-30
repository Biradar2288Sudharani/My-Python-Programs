# MulTableExceptionEx.py
# WAPP which will generate a multiplication table provided by the following condition must be satisfied.
''' --> CONDITIONS <--
1. Generate the exceptions when the number is negative.
2. Generate the exceptions when the number is zero.
3. Generate the multiplication table when the number is positive.
'''
class NagativeNumberError(Exception):pass 
    
class ZeroError(BaseException):pass 

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

try:
    multable(int(input("Enter a number for geneating multiplication table:")))
except ZeroError:
    print("Don't Enter Zero For Mul Table:")
except NagativeNumberError:
    print("Don't Enter Negative Number For Mul Table:")
except ValueError:
    print("Don't Enter alnums,strs and symbols for mul table")
except:
    print("Something Went Wrong Please Check It!")

  