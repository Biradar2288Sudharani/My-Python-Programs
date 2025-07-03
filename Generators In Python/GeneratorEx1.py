# GeneratorEx1.py
# Program for demonstrating generator.
def kvrrange(val):
    i=0
    while(i<=val):
        yield i
        i=i+1
# Main Program
r=kvrrange(10)
print("Type of kvrrande=",type(kvrrange))  # Type of kvrrande= <class 'function'>
print("Type of r=",type(r))  # Type of r= <class 'generator'>






