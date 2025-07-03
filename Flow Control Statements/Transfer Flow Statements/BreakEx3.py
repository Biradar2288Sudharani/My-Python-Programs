# Demo Example using for loop
# Example 1
s="MISSISSIPI"
for index,ch in enumerate(s):
    if(index==4):
        break
    print("{}".format(ch,),end="")

# Example 2
s="MISSISSIPI"
cnt=s.count("I")
icnt=1
for ch in s:
    if(ch=="I")and(icnt==2):
        break
    else:
        print(ch)
        if(ch=="I"):
            icnt=icnt+1

# Example 3
import sys
s="python"
i=0
while(i<len(s)):
    if(s[i]=="o"):
        sys.exit()
    print("\t\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of for loop!")
print("Other Statements In Program!")
    









