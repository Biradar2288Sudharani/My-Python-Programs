# GlobalsEx2.py
# In this example Local And Global Variable are same.
a=10  # Global Variable
b=20  # Global Variable
c=30  # Global Variable
d=40  # Global Variable

def operations():
    a=100  # Local Variable
    b=200  # Local Variable
    c=300  # Local Variable
    d=400  # Local Variable
    res=a+b+c+d+globals()['a']+globals().get('b')+globals()['c']+globals().get('d')
    print("Sum=",res)

# Main Program
operations()





