# WAPP which will generate one to n numbers by using for loop..
# ForLoopEx1.py
n=int(input("Enter how many number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Numbers within:{}".format(n))
    for i in range(1,n+1):
        print("\t\t {}".format(i))
    
        













