# From_ImportSyntax1.py
from mathinfo import PI as p,E 
from aop import sumop as ap,subop as sp,mulop as mp
from icici import bname as bn, addrs as bs,simpleint as si

print("Value of PI=",p.PI)
print("Value of E=",E)
print("*"*50)

ap.sumop(10,20)
sp.subop(10,20)
mp.mulop(10,20)
print("*"*50)

print("Bank Name={}".format(bn.bname))
print("Bank Address={}".format(bs.addrs))
si.simpleint()


