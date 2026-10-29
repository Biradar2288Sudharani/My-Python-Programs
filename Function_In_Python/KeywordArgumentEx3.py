# KeywordArgumentEx3.py
def dispstudinfo(sno,sname,smarks,sbranch="CSE",scountry="Bharat"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,sbranch,scountry))
# Main Program
print("*"*50)
print("\tSNO,\tSNAME\tSMARKS\tSBRANCH\tSCOUNTRY")
print("*"*50)
dispstudinfo(10,"sudha",75)
dispstudinfo(20,"sudeep",76)
dispstudinfo(30,"suhas",46)
dispstudinfo(sname="sunil",sno=40,smarks=78.44)
dispstudinfo(50,sbranch="CIVIL",scountry="USE",sname="sumit",smarks=87)
print("*"*50)








