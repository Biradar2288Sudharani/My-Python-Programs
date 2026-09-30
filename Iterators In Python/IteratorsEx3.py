# IteratorsEx3.py
#Program for demonstrating iterator
x=[10,"sudha",3.14,True,2+3j]
print("Type Of x=",type(x))  # <class,'list'>
# Convert iterable list into ierator object
iterobj=iter(x)
print("Type of iterobj=",type(iterobj))  # <class,list-iterator>
print("*"*50)
print(next(iterobj))
print(next(iterobj))
while(True):
    try:
        print(next(iterobj))
    except StopIteration:
        break
print("*"*50)









