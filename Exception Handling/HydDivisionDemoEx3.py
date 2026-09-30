# HydDivisionDemoEx3.py
from HydDivisionEx2 import divop
from HydEx1 import HydDivisionError
try:
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    res=divop(a,b)   # Function Call --- Either gives result or exception
except HydDivisionError:
    print("\t\t Don't Enter Zero By Denominator")
except:
    print("Something went wrong check it--!!")
else:
    print("Div=",res)
finally:
    print("I am from finally block!!!")









