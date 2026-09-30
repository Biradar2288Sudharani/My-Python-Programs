# EmpPickEx1.py
# Program for accepting employee details and save them in file by using pickling process-------program 1
import pickle
def saveempdatda():
    with open("Employee.data","ab") as fp:
        # accept employees values
        eno=int(input("Enter Employee Number:"))
        ename=input("Enter Employee Name:")
        esal=float(input("Enter Employee Salary:"))
        edsg=input("Enter Employee Designation:")
        # place the employee in list object
        emplst=list()
        emplst.append(eno)
        emplst.append(ename)
        emplst.append(esal)
        emplst.append(edsg)
        # save the emplst data file to file
        pickle.dump(emplst,fp)
        print("Employee data saved into file successfully!!!!")
# Main Program
saveempdatda()

















