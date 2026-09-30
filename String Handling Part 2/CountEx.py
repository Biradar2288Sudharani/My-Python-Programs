# Count Example.py
# Example 1
a="sudharani"
print(a.count("s")) #1
print(a.count("u")) #1
print(a.count("d")) #1
print(a.count("h")) #1
print(a.count("a")) #2
print(a.count("r")) #1
print(a.count("n")) #1
print(a.count("i")) #1

# Example 2
a="MISSISSIPI"
print(a.count("i")) # 0
print(a.count("M")) #1
print(a.count("I")) #4
print(a.count("S")) #4
print(a.count("P")) #1

# Example 3
a="MISSISSIPI"
b=set(a)
print(b)
for ch in b:
    print(ch,"-->",a.count(ch))
'''ANSWER
{'S', 'M', 'P', 'I'}
S --> 4
M --> 1
P --> 1
I --> 4
'''

# Example 4
a="ABRAKADABRA"
b=set(a)
print(b)
for ch in b:
    print(ch,"-->",a.count(ch))
'''ANSWER
{'A', 'R', 'K', 'D', 'B'}
A --> 5
R --> 2
K --> 1
D --> 1
B --> 2
'''

