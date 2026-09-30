# WAPP which will calculate (a*m)*n , a**(m*n)
# ArithmeticOperation6.py
a=int(input("Enter value of a:"))
m=int(input("Enter value of m:"))
n=int(input("Enter value of n:"))
res=(a**m)**n
res1=a**(m*n)
print("Result of ({})({})({})={}".format(a,m,n,res))
print("Result of ({})({})({})={}".format(a,m,n,res1))
