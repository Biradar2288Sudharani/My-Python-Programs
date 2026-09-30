# DefaultArgumentEx1.py
def dispstudinfo1(sno,sname,smarks,sbranch="CSE",scountry="Bharat"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,sbranch,scountry))
def dispstudinfo2(sno,sname,smarks,sbranch="CIVIL",scountry="India"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,sbranch,scountry))
# Main Program
print("*"*50)
dispstudinfo1(10,"sudha",83)
dispstudinfo1(20,"suhas",84)
dispstudinfo2(30,"sudeep",83)
dispstudinfo2(20,"suhas",84,sbranch="MECH",scountry="USA")
print("*"*50)
print("*"*50)
print("\tSNO\tSNAME\tSMARKS\tSBRANCH\tSCOUNTRY")
print("*"*50)
dispstudinfo2(10,"sudha",83)
dispstudinfo2(20,"suhas",84)
dispstudinfo2(30,"sumit",85,"CIVIL")
dispstudinfo2(40,"sunil",86)
dispstudinfo2(40,"sudeep",86,scountry="USA")








