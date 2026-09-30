# EmpUnPickEx2.py
# WAPP which will accept any employee number and optain other details of employee.
import pickle
def searchemprecords():
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Employee.data","rb") as fp:
        eno=int(input("Enter employee number for getting other details:"))
        while(True):
            try:
                emprec=pickle.load(fp)
                if(int(emprec[0])==eno):
                    print("Employee Name:{}".format(emprec[1]))
                    print("Employee Salary:{}".format(emprec[2]))
                    print("Employee Designation:{}".format(emprec[3]))
                    break
            except EOFError:
                print("Employee Record:{} Employee Number Does Not Exist".format(eno))
                break
# Main Program
searchemprecords()


''' --> ANSWER <--
Enter employee number for getting other details:2
Employee Name:sudha
Employee Salary:20000000.0
Employee Designation:manager
'''







