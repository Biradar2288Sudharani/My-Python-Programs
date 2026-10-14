# ConstructEx2.py
class student:
    def __init__(self,sno,sname):  # Default or Parameter -- less constructor
        print("I am from default constructor")
        self.sno=sno
        self.sname=sname

# Main Program
s1=student(100,"sudha")  # object creation ---- makes the pvm to call parameterized constructor.
print("Content of s1=",s1.__dict__)
s2=student(200,"sudharani")  # object creation ---- makes the pvm to call parameterized constructor.
print("Content of s2=",s2.__dict__)
s3=student(300,"suhas")  # object creation ---- makes the pvm to call parameterized constructor.
print("Content of s3=",s3.__dict__)



