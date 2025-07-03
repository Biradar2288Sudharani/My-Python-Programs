# ContinueEx1.py
# Example 1

s="python" #my requirement is to display "pyhon"
for ch in s:  # <-- using for loop
    if(ch=="t"):
        continue
    print(ch)
else:
    print("I am from else part of for loop!")

'''
# Example 2
s="python"
i=0
while(i<=len(s)):   # <-- using while loop
    if(s[i]=="t"):
        continue
    print(s[i])
    i=i+1
else:
    print("I am from else part of while loop!")
'''

# Example 3
s="python" #my requirement is to display "pyhn"
for ch in s:  # <-- using for loop
    if(ch=="t")or(ch=="o"):
        continue
    print(ch)
else:
    print("I am from else part of for loop!")

# Example 4
s="python"
i=0
while(i<=len(s)):   # <-- using while loop
    if(s[i]=="t"):
        continue
    print(s[i])
    i=i+1
else:
    print("I am from else part of while loop!")


# Example 5
s="python"
i=0
while(i<=len(s)):   # <-- using membership operator
    if(s[i] in ["t","o","y"] ):
        continue
    print(s[i])
    i=i+1
else:
    print("I am from else part of while loop!")










