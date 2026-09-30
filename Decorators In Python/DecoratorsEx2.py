# DecoratorsEx2.py
# Program for demonstrating decorator.
def getvalu():  # Normal function defined by kvr
    return int(input("Enter any numerical value:"))
def square(gv):  # Outer function call
    def compute():   # Inner function call
        n=gv()
        res=n**2
        return n,res
    return compute
# Main Program
comp=square(getvalu)  # Function call --- taking another function names as parameter --- decorator call.
print("Type of comp=",type(comp))
n,result=comp()
print("Square({})={}".format(n,result))