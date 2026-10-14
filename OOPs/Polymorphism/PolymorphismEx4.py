# PolymorphismEx4.py

class circle:  
    def area(self,r):  # Original Method
        self.ac=3.14*r**2
        print("Area Of Circle={}".format(self.ac))

class square(circle):  
    def area(self,s):  # Overriden Method
        self.sa=s*s
        print("Area Of Square={}".format(self.sa))
        super().area(float(input("Enter Radius:")))

class rectangle(square):  
    def area(self,l,b):  # Overriden Method
        self.ar=l*b
        print("Area Of Rectangle={}".format(self.ar))
        print("*"*50)
        super().area(float(input("Enter Side:")))
        

# Main Program
r=rectangle()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")))
