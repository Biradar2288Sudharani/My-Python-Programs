# icici.py
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