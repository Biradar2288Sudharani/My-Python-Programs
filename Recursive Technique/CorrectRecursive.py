import sys
def hello(val,n):
    if(n==0):
        sys.exit()
    else:
        print("Hii{}, Hello how are you".format(val))
        hello(val,n-1)
#main program
hello("Rossum",5)