# PolymorphismEx10.py

class circle:  
    def __init__(self,r):  # Original Constructor
        self.ac=3.14*r**2
        print("Area Of Circle={}".format(self.ac))
 
class square:  
    def __init__(self,s):  # Overriden Method
        self.sa=s*s
        print("Area Of Square={}".format(self.sa))

class rectangle(circle,square):  
    def __init__(self,l,b):  # Overriden Method
        self.ar=l*b
        print("Area Of Rectangle={}".format(self.ar))
        print("*"*50)
        square.__init__(self,float(input("Enter Side:")))
        print("*"*50)
        circle.__init__(self,float(input("Enter Radius:")))

# Main Program
r=rectangle(float(input("Enter Length:")),float(input("Enter Breadth:")))


















