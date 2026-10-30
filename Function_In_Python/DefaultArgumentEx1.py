# DefaultParameterEx1.py
def dispstudinfo(sno,sname,smarks,sbranch="CSE",scountry="Bharat"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,sbranch,scountry))
# Main Program
print("*"*50)
print("\tSNO\tSNAME\tSMARKS\tSBRANCH\tSCOUNTRY")
print("*"*50)
dispstudinfo(10,"sudha",83)
dispstudinfo(20,"suhas",84)
dispstudinfo(30,"sumit",85,"CIVIL")
dispstudinfo(40,"sunil",86)
dispstudinfo(40,"sudeep",86,scountry="USA")


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