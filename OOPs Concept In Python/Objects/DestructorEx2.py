# DestructorEx2.py
import time
from os import sys
class employee:
    def __init__(self,eno,ename):   # Parameterized Constructor
        print("*"*30)
        print("I am from parameterized constructor!!")
        self.eno=eno
        self.ename=ename
        print("\t Employee Number:{}".format(self.eno))
        print("\t Employee Name:{}".format(self.ename))
        print("*"*30)
    def __del__(self):   # Destructor Defination
        global totmem
        print("\t Garbage Collector Call __del__(self) --- for deallocating memory space!!")    
        totmem=totmem-sys.getsizeof(self)
        print("\t At present total memory space:{}".format(totmem))     

# Main Program
print("Program Execution Started!!!")
eo1=employee(100,"sudha")  # Object creation --- makes PVM to call parameterized constructor.
eo2=employee(200,"suman")  # Object creation --- makes PVM to call parameterized constructor.
eo3=employee(300,"suhas")  # Object creation --- makes PVM to call parameterized constructor.
totmem=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("Initial total memory space of current program=",totmem)  # 144
print("Program Execution End!!!")
time.sleep(10)

















