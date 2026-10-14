# GarbageCollectorEx2.py
import time,sys
import gc
class employee:
    def __init__(self,eno,ename):  # Parameterized Constructor
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
print("\t Initially, Is Garbage Collector Running=",gc.isenabled)  # True
print("*"*50)
eo1=employee(100,"sudha")  # Object creation --- makes PVM to call parameterized constructor.
eo2=employee(200,"suman")  # Object creation --- makes PVM to call parameterized constructor.
eo3=employee(300,"suhas")  # Object creation --- makes PVM to call parameterized constructor.
totmem=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("Initial total memory space of current program=",totmem)  # 144
print("Program Execution End!!!")
print("*"*50)
print("\t Now, Is Garbage Collector Running=",gc.isenabled)  # False
time.sleep(10)            








                                                         
