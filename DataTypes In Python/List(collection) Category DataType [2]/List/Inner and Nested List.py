# Inner or nested list
a=[10,"sudha",[1,2,3],[10,20,30],"amma"]
print(a,type(a),id(a))
for val in a:
    print(val,type(val),type(a))
    
print(a[0])
print(a[2])
print(a[-3])
print(a[3])
print(a[-2])
print(a[2][1])
print(a[2][-2])
print(a[-3][1])
print(a[-3][-2])
print(a[2][1:3])
print(a[2][1:])
print(a[2][-2:])
print(a[3][0::2])
print(a[3][::2])
print(a[3][0:3:2])
print(a[-2][-3::2])

a[2][1]=100
print(a)
a[-2][-2]=50
print(a)
a[-2][::2]=[72,75]
print(a)
a[2].append(15)
print(a)
a[-2].insert(1,80)
print(a)
a[-2].sort(reverse=True)
print(a)
del a[-2][1:]
print(a)
del a[2][::2]
print(a)
a[2].clear()
print(a)
a[-2].remove(80)
del a[2:4]
print(a)
a.insert(2,[15,18,13])
print(a)
a.insert(-1,[20,15,10])
print(a)

























