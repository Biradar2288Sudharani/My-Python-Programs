print("--> Substract <--")
from collections import Counter
c1=Counter(a=4,b=3,c=10)
c2=Counter(a=10,b=3,d=4)
c=c1.subtract(c2)
print(c)