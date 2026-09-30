# WAPP which will calculate square root of any number(Without using sqrt function of math module) 
n=int(input("Enter a number for getting its sqrt root:"))
res=n**0.5
print("Square root({})={}".format(n,res))
print("Square root((%f)=%0.2f" %(n,res))
print("Square root ({})={}".format(n,round(res,2)))
