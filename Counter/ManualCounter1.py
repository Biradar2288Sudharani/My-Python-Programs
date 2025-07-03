# program for finding number of occurances of a word iterable object
# ManualCounter.py
s=input("Enter a Word")
d={} #Empty dict
for ch in s:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]=d[ch]+1
else:
    print("content of d=",d)