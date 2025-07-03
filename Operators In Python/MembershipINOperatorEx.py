# MembershipINOperatorEx.py
print("p" in "python")
print("k" in "python")

# Example 1
a="Python"
print("P"  in "Python")
print("p"  in "Python")
print("k"  in "Python")
print("y"  in "Python")
print("s"  in "Python")

# Example 2
a="Python"
print("PYT"  in "Python")
print("pyt"  in "Python")
print("Pyt"  in "Python")
print("yth"  in "Python")
print("son"  in "Python")

# Example 3
a="PYTHON"
print("PO"  in "a")
print("NOH"  in "a")
print("NOH"  in a[::-1])
print("pyt"  in a[::-1])
print("PTO"  in a[::2][::-1])
print("PTO"  in a[::2][::-1][::-1])
print("PTO"  in a[-2::-2])
print("PTO"[::-1]  in a[-2::-2][::-1])
print(a  in a)

# Example 4
a=["sudha",100,3.14,True,2+3j]
print("sum" in a)
print("sum" in a[0])
print("sudha" in a[0])
# print("sum" in a[1])-->TypeError: argument of type 'int' is not iterable
# print(2 in a[-1])-->TypeError: argument of type 'complex' is not iterable

# Example 5
a={10:"apple",20:"mango",30:"kiwi"}
print("apple"  in a)
print("10"  in a)
print("60"  in a)
print(a[10][::-1]  in a.get(10)[::])
print(a.get(100)  in a)

# Example 6
a="apple is red color"
print("e" in a)
print("e"[::-1] in a)

