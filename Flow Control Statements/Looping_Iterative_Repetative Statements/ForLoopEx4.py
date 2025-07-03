# WAPP which will calculate sum of cubes and squares of n natural numbers. where n is positive
# ForLoopEx4.py
n=int(input("Enter how many natural number squares sum you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Number \t\t Cubes Of Natural Numbers \t\t Squares Of Natural Numbers")
    s,cs,ss=0,0,0
    for i in range(1,n+1):
        print("\t{}\t\t\t{}\t\t\t\t\t\t\t".format(i,i**3,i**2))
        s=s+i
        cs=cs+i
        ss=ss+i
    else:
        print("\t{}\t\t\t{}\t\t\t\t\t\t\t".format(s,cs,ss))


'''
Here s=sum
     ss=square sum
'''















