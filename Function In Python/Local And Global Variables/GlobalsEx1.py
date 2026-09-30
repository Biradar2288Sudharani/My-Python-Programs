# GlobalsEx1.py
# Demo Example
a=10  # Global Variable
b=20  # Global Variable
def operations():
    a=100  # Global Variable
    b=200  # Global Variable
    obj=globals()
    print("All Global Variables")
    print("*"*50)
    for gvn,gvv in obj.items():
        print("\t{}-->".format(gvn,gvv))
    print("*"*50)
    print("Programmer Defined Global Variable Way-1")
    print("*"*50)
    print("Global Variable-a:{}".format(obj.get('a')))
    print("Global Variable-a:{}".format(obj.get('b')))
    print("*"*50)
    print("Programmer Defined Global Variable Way-2")
    print("*"*50)
    print("Global Variable-a:{}".format(obj['a']))
    print("Global Variable-a:{}".format(obj['b']))
    print("*"*50)
    print("Programmer Defined Global Variable Way-3")
    print("*"*50)
    print("Global Variable-a:{}".format(globals()['a']))
    print("Global Variable-a:{}".format(globals()['b']))
    print("*"*50)
    print("Programmer Defined Global Variable Way-4")
    print("*"*50)
    print("Global Variable-a:{}".format(globals().get('a')))
    print("Global Variable-a:{}".format(globals().get('b')))
    
# Main Program
operations()  # Function Call






