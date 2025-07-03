print("--> Counter <--")
from collections import Counter
a="aaaaabbbbbbbbbcccchhhhhhsssssskkkkkkkk"
b=Counter(a)
print(b)

print("--> elements() Function <--")
from collections import Counter
a=Counter(a=1,b=2,c=3,d=4,e=5,f=6)
for val in a.elements():
    print(val, end=" ")

print("--> elements() Function <--")
from collections import Counter
a=Counter(a=1,b=2,c=3,d=4,e=5,f=6,k=0)
for val in a.elements():
    print(val, end=" ")

print("--> elements() Function <--")
from collections import Counter
a=Counter(a=1,b=2,c=3,d=4,e=5,f=6,k=-2)
for val in a.elements():
    print(val, end=" ")

print("--> most_common(value) Function <--")
from collections import Counter
a="aaaaabbbbbbbbbcccchhhhhhsssssskkkkkkkk"
b=Counter(a)
print(b)
c=b.most_common(1)
print(c)
c=b.most_common(2)
print(c)


print("--> Substract <--")
from collections import Counter
c1=Counter(a=4,b=3,c=10)
c2=Counter(a=10,b=3,d=4)
c=c1.subtract(c2)
print(c)




