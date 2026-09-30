# WAPP which will generate all the odd numbers by using for loop where n can be positive. 
# ForLoopEx3.py
n=int(input("Enter how many Number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Odd Numbers Within in : {}".format(n))
    for i in range(1,n+1,2):
        print("\t\t {}".format(i))


















