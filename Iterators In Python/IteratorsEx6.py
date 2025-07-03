# IteratorsEx6.py
# Program for demonstrating iterator
x={10:"sudha",20:"shankar",30:"sanu",40:"chittu"}
print("Type Of x=",type(x))  # <class,'dict'>
# Convert iterable dict into ierator object
iterobj=iter(x)
print("Type of iterobj=",type(iterobj))  # <class,dict-iterator>
for val in iterobj:
    print(val)




