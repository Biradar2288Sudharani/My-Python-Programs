# Demo Example using while loop
# my requirement is to display "sudha" without using indexing and slicing
# BreakEx2.py
s="sudharani"
i=0
while(i<len(s)):
    if(s[i]=="r"):
        break
    print("\t\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of for loop!")



















