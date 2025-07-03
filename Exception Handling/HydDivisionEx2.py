# HydDivisionEx2.py ---- File name and module name
from HydEx1 import HydDivisionError
def divop(a,b):
    if(b==0):
        raise HydDivisionError   # Hitting the exception explicitely by the programmer
    else:
        return(a/b)