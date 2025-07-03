# Non-InhProg.py
# Program for denmonstrating Non-Inheristance
class BC:
    def getA(self):
        self.a=10
class DC:
    def getA(self):
        self.b=20

# Main Program
bo1=BC()
do1=DC()
print(" bo1 content=",bo1.__dict__)
print(" do1 content=",do1.__dict__)
print("*"*50)
bo1.getB() # Gives Attribute Error
do1.getB()
do1.getA()  # Gives Attribute Error
bo1.getA()
print(" bo1 content=",bo1.__dict__)
print(" bp2 content=",do1.__dict__)
print("*"*50)














