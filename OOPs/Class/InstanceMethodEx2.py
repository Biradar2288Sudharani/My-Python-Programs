# InstanceMethodEx2.py
class sum:
    def readvalues(self):
        self.a=float(input("Enter First Value:"))
        self.b=float(input("Enter Second Value:"))
        
    def disp(self):
        self.readvalues()
        self.addop()
        print("Value of a=",self.a)
        print("Value of b=",self.b)
        print("Sum=",self.c)        

# Main Program
s1=sum()
s1.disp()





