# WAPP which will accept list of values and display only primes.
# OnlyPrimeEx.py
lst=list()  # empty list for storing randomvalues
print("Enter list of random values and press @ to stop:")
while(True):
    value=input()
    if(value=="@"):
        break
    lst.append(int(value))
print("List of Values:{}".format(lst))
# code for random primes
plist=[]
for num in lst:  # Outer Loop
    if(num<=1):
        continue
    res=True
    for i in range(2,num):  # Inner Loop
        if(num%i==0):
            res=False
            break
    if(res):
        plist.append(num)
    else:
        print("List of Primes={}".format(plist))










