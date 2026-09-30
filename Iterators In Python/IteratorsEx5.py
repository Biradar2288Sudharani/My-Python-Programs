# IteratorsEx5.py
#Program for demonstrating iterator
x={10,20,30,40,"hyd","python"}
print("Type Of x=",type(x))  # <class,'set'>
# Convert iterable set into ierator object
iterobj=iter(x)
print("Type of iterobj=",type(iterobj))  # <class,set-iterator>
for val in iterobj:
    print(val)





