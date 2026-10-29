# KeywordVariableLengthArguEx5.py
def findtotal(sno,sname,sbranch,**submarks):
    print("*"*50)
    print("\t Student Number:{}".format(sno))
    print("\t Student Name:{}".format(sname))
    print("\t Student Branch:{}".format(sbranch))
    print("*"*50)
    for subject,mark in submarks.items():
        print("\t {} --> {}".format(subject,mark))

# Main Progrma
findtotal(100,"Sudha","CSE",Python=90,DBMS=69,AI=78,JAVA=90)
findtotal(200,"Suman","IT",Python=90,DBMS=69,DS=78,DSA=90)

