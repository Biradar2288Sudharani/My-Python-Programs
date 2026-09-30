# EmpUnPickEx1.py
# Program for accepting employee details and save them in file by using pickling process-------program.
import pickle
def reademprecords():
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Employee.data","rb") as fp:
        print("*"*50)
        while(True):
            try:
                emprec=pickle.load(fp) # emprec is an object of list.
                for val in emprec:
                    print("{}".format(val),end=" \t ")
                print()
            except EOFError:
                print("*"*50)
                break
# Main Program
reademprecords()










