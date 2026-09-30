# GlobalKeywordEx4.py
def incr1():
    global a,b  # Mandatory to use global keyword
    a=a+1
    b=b+1

def incr2():
    global a,b  # Mandatory to use global keyword
    a=a+10
    b=b+10

def getAB():
    k=a+1
    v=b+1
    r=a+b
    print("In getAB()---Local Variables --> k={},v={},r={}".format(k,v,r))

# Main Program
a,b=10,20  # Global Variable
print("In main program before incr1()-->a:{} \t b:{}".format(a,b)) 
incr1()  # Function Call
print("In main program after incr1()-->a:{} \t b:{}".format(a,b)) 
incr2()  # Function Call
print("In main program after incr2()-->a:{} \t b:{}".format(a,b))
getAB()  # Function Call

















