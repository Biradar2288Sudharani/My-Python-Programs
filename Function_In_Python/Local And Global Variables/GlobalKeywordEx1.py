# GlobalKeywordEx1.py
def incr1():
    a=a+1
# Main Program
a=10  # Global Variable
print("Value of a in main program before incr1()={}".format(a))
incr1()
print("Value of a in main program after incr1()={}".format(a))

'''  --> ANSWER <--
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
'''
