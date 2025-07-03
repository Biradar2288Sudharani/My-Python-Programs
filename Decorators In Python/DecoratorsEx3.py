# DecoratorsEx3.py
def square(gv):
    def call():
        n=gv()
        res=n**2
        return n,res
    return call
@square
def getvalue():  # Normal function defined by kvr
    return int(input("Enter any numerical value:"))
# Main Program
n,res=getvalue()
print("Square({})={}".format(n,res))





