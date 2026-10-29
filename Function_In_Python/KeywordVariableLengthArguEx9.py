# KeywordVariableLengthArguEx8.py
def findtotal(sno,sname,sbranch,*nums,scity="HYD",**submarks):
    print("*"*50)
    print("\t Student Number:{}".format(sno))
    print("\t Student Name:{}".format(sname))
    print("\t Student Branch:{}".format(sbranch))
    print("\t Student City:{}".format(scity))
    print("Variable Length Argument")
    for val in nums:
        print("{}".format(val),end=" ")
    print()
    print("*"*50)
    totalmarks=0
    for subject,mark in submarks.items():
        print("\t {} --> {}".format(subject,mark))
        totalmarks=totalmarks+mark
    else:
        print("*"*50)
        print("TotalMarks:{}".format(totalmarks))

# Main Program
findtotal(100,"Sudha","CSE",10,20,30,40,Python=90,DBMS=69,AI=78,JAVA=90)
findtotal(200,"Suman","IT",100,200,300,Python=90,DBMS=69,DS=78,DSA=90)
findtotal(300,"Sushil","MECH",101,202,303,404,P=90,D=69,A=78,J=90,scity="BANG")
findtotal(400,"Suhas","CIVIL",1000,2000,3000,Py=90,DB=69,SD=78,DA=90)

