# GeneratorEx2.py
# Program for demonstrating generator.
def kvrrange(val):
    i=0
    while(i<=val):
        yield i
        i=i+1
# Main Program
import sys
r=kvrrange(5)  # Provide thr 0 to 10 only on demand.
print("Type of kvrrande=",type(kvrrange))  # Type of kvrrande= <class 'function'>
print("Type of r=",type(r))  # Type of r= <class 'generator'>
print("*"*50)
while(True):
    try:
        print(next(r))
    except StopIteration:
        print("*"*50)
        break




