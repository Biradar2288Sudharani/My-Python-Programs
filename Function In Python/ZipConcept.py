# ZipConcept.py
lst1=[10,20,30,40,50]
lst2=["suman","suvesh","suhas","sumit","sudha"]
z=zip(lst1,lst2)
print(z,type(z))  # <zip object at 0x0000016FEB741E40> <class 'zip'>
for x,y in z:
    print("{}\t{}".format(x,y))

''' --> ANSWER <--
<zip object at 0x0000016FEB741E40> <class 'zip'>
10      suman
20      suvesh
30      suhas
40      sumit
50      sudha
'''