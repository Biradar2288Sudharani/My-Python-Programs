# KeywordVariableLengthArguEx7.py
def findtotal(sno,sname,sbranch,**submarks,scity="HYD"):
    print("*"*50)
    print("\t Student Number:{}".format(sno))
    print("\t Student Name:{}".format(sname))
    print("\t Student Branch:{}".format(sbranch))
    print("\t Student City:{}".format(scity))
    print("*"*50)
    totalmarks=0
    for subject,mark in submarks.items():
        print("\t {} --> {}".format(subject,mark))
        totalmarks=totalmarks+mark
    else:
        print("*"*50)
        print("TotalMarks:{}".format(totalmarks))

# Main Program
findtotal(100,"Sudha","CSE",Python=90,DBMS=69,AI=78,JAVA=90)
findtotal(200,"Suman","IT",Python=90,DBMS=69,DS=78,DSA=90)

''' --> ANSWER <--
SyntaxError: arguments cannot follow var-keyword argument
In this example error is generated line No:2 
'''







