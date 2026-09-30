# IteratorsEx4.py
#Program for demonstrating iterator
x=(10,"sudha",3.14,True,2+3j)
print("Type Of x=",type(x))  # <class,'tuple'>
# Convert iterable list into ierator object
iterobj=iter(x)
print("Type of iterobj=",type(iterobj))  # <class,tuple-iterator>
for val in iterobj:
    print(val)




