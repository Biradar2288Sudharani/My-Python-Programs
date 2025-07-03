# BasicFunctionEx3.py
def dispvalues(lst):
    print("----------------")
    print("Type of lst=",type(lst))
    for val in lst:
        print(val)
    print("-------------")
    
# main Program
lst1=[10,"anna",3.14,True,3+2j]   
dispvalues(lst1)          # Function Call with list object
tuple=(10,20,30,40)      
dispvalues(tuple)         # Function Call with tuple object
set={10,"anna",3.14,True,3+2j}     
dispvalues(set)           # Function Call with set object
dict={10:"python",20:"cpp",30:"C",40:"java"}   
dispvalues(dict)          # Function Call with dict object