# DestructorEx1.py
import time
class employee:
    def __init__(self,eno,ename):   # Parameterized Constructor
        print("*"*30)
        print("I am from parameterized constructor!!")
        self.eno=eno
        self.ename=ename
        print("\t Employee Number:{}".format(self.eno))
        print("\t Employee Name:{}".format(self.ename))
    def __del__(self):   # Destructor Definatio
        print("Garbage Collector Call __del__(self) --- for deallocating memory space!!")         

# Main Program
print("Program Execution Started!!!")
eo1=employee(100,"sudha")  # Object creation --- makes PVM to call parameterized constructor.
eo2=employee(200,"suman")  # Object creation --- makes PVM to call parameterized constructor.
eo3=employee(300,"suhas")  # Object creation --- makes PVM to call parameterized constructor.
print("Program Execution End!!!")
time.sleep(10)






