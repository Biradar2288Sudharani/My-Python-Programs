# WAPP which will calculate simple interest and total amount to pay by using function
# SimpleInterestEx.py
#  simple_interest = (principal * rate * time) / 100
#  total_amount = principal + simple_interest
'''
def sita(p,r,t):
    si=(p*r*t)/100
    return si
    ta=p+si
    return ta
# Main Program
x=float(input("Enter principle amount:"))
y=float(input("Enter rate:"))
z=float(input("Enter time:"))
res=sita(x,y,z)
print("Simple Interest and Total Amount({},{},{})={}".format(x,y,z,res))
print("-------------")
p=float(input("Enter p:"))
r=float(input("Enter r:"))
t=float(input("Enter t:"))
result=sita(p,r,t)
print("Simple Interest and Total Amount=".format(p,r,t,result))
'''

def si(p,r,t):
    si=(p*r*t)/100
    print("SI({},{},{})={}".format(p,r,t,si))
    ta=p+si
    print("TA({},{})={}".format(p,si,ta))
# main program
p=float(input("Enter principle amount:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
si(p,r,t)

