# MulTableDemo.py
from MulTable import multable
from MulExcept import ZeroError, NagativeNumberError
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








