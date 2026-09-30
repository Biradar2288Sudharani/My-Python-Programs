# Non-DistEx1.py
# Program for demonstrating destructors
class employee:
    def __init__(self,eno,ename):   # Parameterized Constructor
        print("*"*30)
        print("I am from parameterized constructor!!")
        self.eno=eno
        self.ename=ename
        print("\t Employee Number:{}".format(self.eno))
        print("\t Employee Name:{}".format(self.ename))
        print("*"*30)
# Main Program
eo1=employee(100,"sudha")  # Object creation --- makes PVM to call parameterized constructor.
eo2=employee(200,"suman")  # Object creation --- makes PVM to call parameterized constructor.
eo3=employee(300,"suhas")  # Object creation --- makes PVM to call parameterized constructor.














