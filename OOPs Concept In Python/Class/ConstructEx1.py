# ConstructEx1.py
class student:
    def __init__(self):  # Default or Parameter -- less constructor
        print("I am from default constructor")
        self.sno=100
        self.sname="sudha"

# Main Program
s1=student()  # object creation ---- makes the pvm to call default constructor.
print("Content of s1=",s1.__dict__)
s2=student()  # object creation ---- makes the pvm to call default constructor.
print("Content of s2=",s2.__dict__)
s3=student()  # object creation ---- makes the pvm to call default constructor.
print("Content of s3=",s3.__dict__)



