# WAPP which will accept numerical value & find the sum of it's digits.
# ForLoopEx6.py
'''
Example:
given input: 1256
expected output: 14(1+2+5+6)
Test Case 1: GIven value must be number
Test Case 2:Given value should not be str , alnums, and symbols.
'''
n=input("Enter a Number:")
s=0
for digit in n:
    v=int(digit)
    s=s+v
else:
    print("Sum of Digits ({})={}".format(n,s))
    if(n.isalpha()):
        print("is invalid input".format(n))
    elif(n.isalnum()):
        print("is invalid input".format(n))
    else:
        print("Program Execution Is Done!!")

'''
if(n.isalpha()):
    print("{} is invalid input".format(n))
elif(n.isalnum()):
    print("{} is invalid input".format(n))
else:
    print("Program Execution Is Done!!")
'''



















