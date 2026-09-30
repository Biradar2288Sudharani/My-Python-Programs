# ModuleDemoEx1.py
# Example 1
PI=3.14
E=2.71
print("Value of PI=",PI)
print("Value of E=",E)
print("*"*50)

''' --> ANSWER <--
Value of PI= 3.14
Value of E= 2.71
'''

# Example 2
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

''' --> ANSWER <--
Sum(10,20)=30
Sub(10,20)=30
Mul(10,20)=200
'''

# Example 3
bname="ICICI"
addrs="AMPT-HYD"
def simpleint():
    p=float(input("Enter Principle Amount:"))
    r=float(input("Enter Rate Of Interest:"))
    t=float(input("Enter Time:"))
    # Calculate Simple Interest(simpleint)
    si=(p*t*r)/100
    totamt=p+si
    print("*"*40)
    print("\t Principle Amount:{}".format(p)) 
    print("\t Rate of Interest:{}".format(r))
    print("\t Time:{}".format(t))
    print("\t Simple Interest:{}".format(si))  
    print("\t Total Amount To Pay:{}".format(totamt))
    print("*"*50)
# Main Program
print("Bank Name={}".format(bname))
print("Bank Address={}".format(addrs))
simpleint()

''' --> ANSWER <--
Bank Name=ICICI
Bank Address=AMPT-HYD
Enter Principle Amount:4000
Enter Rate Of Interest:12
Enter Time:5
**************************************************
         Principle Amount:4000.0
         Rate of Interest:12.0
         Time:5.0
         Simple Interest:2400.0
         Total Amount To Pay:6400.0
**************************************************
'''



