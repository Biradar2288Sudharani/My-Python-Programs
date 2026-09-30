# WAPP which will accept any digit & display the name of digit
# if-elif-elseStmtEx1.py
digit={0:"One",1:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
dig=int(input("Enter Your Digit:"))
res=digit.get(dig) if digit.get(dig)!=None else "Is Positive Number"
print("{} is {}".format(dig,res))
# OR ---
res=digit.get(dig) if digit.get(dig)!=None else "Is Positive Number" if dig>0 else " Is Negative Number"
print("{} is {}".format(dig,res))
# OR---
print("{} is {}".format(digit.get(dig) if digit.get(dig)!=None else "Is Positive Number" if dig>0 else " Is Negative Number",(dig,res)))


















