# GlobalKeywordEx3.py
def incr1():
    global a,b
    a=a+1
    b=b+1

def incr2():
    global a,b
    a=a+10
    b=b+10

# Main Program
a,b=10,20  # Global Variable
print("In main program before incr1()-->a:{} \t b:{}".format(a,b)) 
incr1()  # Function Call
print("In main program after incr1()-->a:{} \t b:{}".format(a,b)) 
incr2()  # Function Call
print("In main program after incr2()-->a:{} \t b:{}".format(a,b))








