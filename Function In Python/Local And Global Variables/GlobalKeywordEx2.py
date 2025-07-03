# GlobalKeywordEx2.py
def incr1():
    global a
    a=a+1

def incr2():
    global a
    a=a+10

# Main Program
a=10
print("Value of a in main program before incr1()={}".format(a))
incr1()
print("Value of a in main program after incr1()={}".format(a))
incr2()
print("Value of a in main program after incr2()={}".format(a))












