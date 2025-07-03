# WAPP which will calculate a*m/a*n
# ArithmeticOperation5.py            
a=int(input("Enter value of a:"))
m=int(input("Enter value of m:"))
n=int(input("Enter value of n:"))
res=(a**m)/(a**n)
res1=a**m*a**(-n)
res2=a**(m-n)
print("Result of ({})({})({})={}".format(a,m,n,res))
print("Result of ({})({})({})={}".format(a,m,n,res1))
print("Result of ({})({})({})={}".format(a,m,n,res2))