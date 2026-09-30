# DecoratorsEx4.py
# Program for without decorator
def getvalue():  # Normal function defined by kvr
    return int(input("Enter any numerical value:"))
def square():
    n=getvalue()
    res=n**2
    print("Square({})={}".format(n,res))
# Main Program
square()






