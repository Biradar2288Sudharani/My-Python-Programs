# ModuleDemoEx2.py
'''
# Example 1
print("PI=",PI)
print("E=",E)

--> ANSWER <--
NameError: name 'PI' is not defined


# Example 2
sumop(10,20)
subop(10,20)
mulop(10,20)

--> ANSWER <--
NameError: name 'sumop' is not defined


# Example 3
print("Bank Name={}".format(bname))
print("Bank Address={}".format(addrs))
simpleint()


--> ANSWER <--
NameError: name 'bname' is not defined

# Here  not able to call it because on eprogram global variables and functions not come one program into another  program.
'''

# Solutions for above 3 examples.

# Example 1
import ModuleDemoEx1
print("Value of PI=",ModuleDemoEx1.PI)
print("Value of E=",ModuleDemoEx1.E)
print("*"*50)

# Example 2
ModuleDemoEx1.sumop(10,20)
ModuleDemoEx1.subop(10,20)
ModuleDemoEx1.mulop(10,20)
print("*"*50)

# Example 3
print("Bank Name={}".format(ModuleDemoEx1.bname))
print("Bank Address={}".format(ModuleDemoEx1.addrs))
ModuleDemoEx1.simpleint()

# This program executed successfully.
# Here impoert is the file name of program or code where is our global and functions are present.
''' --> ANSWERS <--
Value of PI= 3.14
Value of E= 2.71
**************************************************
Sum(10,20)=30
Sub(10,20)=30
Mul(10,20)=200
**************************************************
Bank Name=ICICI
Bank Address=AMPT-HYD
Enter Principle Amount:1200
Enter Rate Of Interest:2
Enter Time:4
******************************
         Principle Amount:1200.0
         Rate of Interest:2.0
         Time:4.0
         Simple Interest:96.0
         Total Amount To Pay:1296.0
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
Enter Principle Amount:1200
Enter Rate Of Interest:2
Enter Time:4
******************************
         Principle Amount:1200.0
         Rate of Interest:2.0
         Time:4.0
         Simple Interest:96.0
         Total Amount To Pay:1296.0
**************************************************
'''