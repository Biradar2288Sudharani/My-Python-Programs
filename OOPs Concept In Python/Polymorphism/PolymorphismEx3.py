# PolymorphismEx3.py

class circle:  
    def area(self):  # Original Method
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area Of Circle={}".format(self.ac))

class square(circle):  
    def area(self):  # Overriden Method
        self.s=float(input("Enter Side:"))
        self.sa=self.s*self.s
        print("Area Of Square={}".format(self.sa))

class rectangle(square):  
    def area(self):  # Overriden Method
        self.l=float(input("Enter Length:"))
        self.b=float(input("Enter Breadth:"))
        self.ar=self.l*self.b
        print("Area Of Rectangle={}".format(self.ar))
        print("*"*50)
        circle.area(self)
        print("*"*50)
        square.area(self)

# Main Program
r=rectangle()
r.area()
