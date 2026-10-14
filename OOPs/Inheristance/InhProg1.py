# InhProg1.py

# Program for denmonstrating Inheristance
class BC:
    def getA(self):
        self.a=10
class DC(BC):
    def getB(self):
        self.b=20

# Main Program
do1=DC()
print(" do11 content=",do1.__dict__)
print("*"*50)
do1.getA()
print(" do1 content=",do1.__dict__)
do1.getB() 
print(" do1 content=",do1.__dict__)
print("*"*50)














