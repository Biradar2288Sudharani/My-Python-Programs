# MembershipNOTINOperatorEx.py
print("p" not in "python")
print("k" not in "python")

# Example 1
a="Python"
print("P" not in "Python")
print("p" not in "Python")
print("k" not in "Python")
print("y" not in "Python")
print("s" not in "Python")

# Example 2
a="Python"
print("PYT" not in "Python")
print("pyt" not in "Python")
print("Pyt" not in "Python")
print("yth" not in "Python")
print("son" not in "Python")

# Example 3
a="PYTHON"
print("PO" not in "a")
print("NOH" not in "a")
print("NOH" not in a[::-1])
print("pyt" not in a[::-1])
print("PTO" not in a[::2][::-1])
print("PTO" not in a[::2][::-1][::-1])
print("PTO" not in a[-2::-2])
print("PTO"[::-1] not in a[-2::-2][::-1])
print(a not in a)

# Example 4
a=["sudha",100,3.14,True,2+3j]
print("sum" not in a)
print("sum" not in a[0])
print("sudha" not in a[0])
# print("sum" not in a[1])-->TypeError: argument of type 'int' is not iterable
# print(2 in a[-1])-->TypeError: argument of type 'complex' is not iterable

# Example 5
a={10:"apple",20:"mango",30:"kiwi"}
print("apple" not in a)
print("10" not in a)
print("60" not in a)
print(a[10][::-1] not in a.get(10)[::])
print(a.get(100) not in a)

# Example 6
a="apple is red color"
print("e" not in a)
print("e"[::-1] not in a)











