# IndexExample.py
# Example 1
a="sudharani"
print(a.index("s")) # 0
print(a.index("u")) # 1
print(a.index("d")) # 2
print(a.index("h")) # 3
print(a.index("a")) # 4
print(a.index("r")) # 5
print(a.index("a")) # 6
print(a.index("n")) # 7
print(a.index("i")) # 8
# print(a.index("S")) # ValueError: substring not found

# Example 2
s="NISSON"
for index, ch in enumerate(s):
    print("{}-->{}".format(index , ch))
for index, ch in enumerate(s):
    if(ch=="I"):
        print("{}-->{}".format(index , ch))






