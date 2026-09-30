# WAPP which will generate 1 to n multiplication tables,where n must be positive integer value.
# MulTableEx.py
n=int(input("Enter how many mul table you want:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    for i in range(1,n+1):
        print("="*20)
        print("Mul Table For:{}".format(i))
        print("="*20)
        for j in range(1,11):
            print("\t\t {}*{}={}".format(i,j,i*j))
        else:
            print("="*20)















