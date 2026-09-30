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








