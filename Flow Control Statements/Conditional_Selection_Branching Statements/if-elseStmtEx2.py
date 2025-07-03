# WAPP which will accept any word & decide whether it is palindrom or not.
# if-elseStmtEx2.py
word=input("Enter any word:")
res=word
if(res==word[::-1]):
    print("Given Word {} is Palindrom".format(res))
else:
    print("Given Word {} is not Palindrom".format(res))
print("Program Execution Is Completed!!")