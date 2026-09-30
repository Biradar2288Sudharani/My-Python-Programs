# WAPP which will generate 1 to n multiplication for random numbers. and read the list of random numbers from keyboard.
# MulTableForRandomNumEx.py
'''
lst=list() # empty list for storing randomvalues
print("Enter list of random values and press @ to stop:")
while(True):
    value=input()
    if(value=="@"):
        break
    lst.append(int(value))
print("List of Values:{}".format(lst))
# code for random numbers multiplication tables
for num in lst:
    if(num<=0):
        print("{} Is Invalid Input--Can't Generate Mul Table".format(num))
        continue
    else:
        for i in range(1,num+1):
            print("="*20)
            print("Mul Table For:{}".format(i))
            print("="*20)
        for j in range(1,11):
            print("\t\t {}*{}={}".format(i,j,i*j))
        else:
            print("="*20)
'''
lst=list() # empty list for storing randomvalues
print("Enter list of random values and press @ to stop:")
while(True):
    value=input()
    if(value=="@"):
        break
    lst.append(int(value))
print("List of Values:{}".format(lst))
# code for random numbers multiplication tables
for num in lst:
    if(num<=0):pass
    else:
        for i in range(1,num+1):
            print("="*20)
            print("Mul Table For:{}".format(i))
            print("="*20)
        for j in range(1,11):
            print("\t\t {}*{}={}".format(i,j,i*j))
        else:
            print("="*20)     















