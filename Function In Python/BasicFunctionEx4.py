# BasicFunctionEx4.py
def dispvalues(lst):
    print("----------------")
    print("Type of lst=",type(lst))
    for val in lst:
        print(val)
    print("----------------")

def dispvalues1(dobj):
    print("----------------")
    print("Type of lst=",type(dobj))
    for k,v in dobj.items():
        print("\t {}-->{}".format(k,v))
    print("----------------")
# main program
lst=[10,"anna",3.14,True,3+2j]
dispvalues(lst) # Function Call










