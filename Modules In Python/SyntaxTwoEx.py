# SyntaxTwoEx.py
import mathinfo , aop, icici

print("Value of PI=",mathinfo.PI)
print("Value of E=",mathinfo.E)
print("*"*50)

aop.sumop(10,20)
aop.subop(10,20)
aop.mulop(10,20)
print("*"*50)

print("Bank Name={}".format(icici.bname))
print("Bank Address={}".format(icici.addrs))
icici.simpleint()


''' --> ANSWER <--
Value of PI= 3.14
Value of E= 2.71
**************************************************
Sum(10,20)=30
Sub(10,20)=30
Mul(10,20)=200
**************************************************
Bank Name=ICICI
Bank Address=AMPT-HYD
Enter Principle Amount:4000
Enter Rate Of Interest:2
Enter Time:4
****************************************
         Principle Amount:4000.0
         Rate of Interest:2.0
         Time:4.0
         Simple Interest:320.0
         Total Amount To Pay:4320.0
**************************************************
Value of PI= 3.14
Value of E= 2.71
**************************************************
Sum(10,20)=30
Sub(10,20)=30
Mul(10,20)=200
**************************************************
Bank Name=ICICI
Bank Address=AMPT-HYD
Enter Principle Amount:2000
Enter Rate Of Interest:3
Enter Time:2
****************************************
         Principle Amount:2000.0
         Rate of Interest:3.0
         Time:2.0
         Simple Interest:120.0
         Total Amount To Pay:2120.0
**************************************************
'''











