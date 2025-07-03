# IteratorsEx7.py
x="Python Program"
print("Type Of x=",type(x))  # <class,'str'>
# Convert iterable str into ierator object
iterobj=iter(x)
print("Type of iterobj=",type(iterobj))  # <class,'str_ascii_iterator'>
for val in iterobj:
    print(val)



