# PolymorphismEx1.py
# WAPP which will calculate area of different figures by using polymorphic approch.

class circle(object):
    def area(self):      # Original Method
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle={}".format(self.ac))
        super().area()

class square(circle):
    def area(self):      # Overriden Method
        self.s=float(input("Enter Side:"))
        self.sa=self.s*self.s
        print("Area of Square={}".format(self.sa))
        print("*"*50)
        # super().area() ---> AttributeError: 'super' object has no attribute 'area'

class rectangle(square):
    def area(self):      # Overriden Method
        self.l=float(input("Enter Length:"))
        self.b=float(input("Enter Breadth:"))
        self.ra=self.l*self.b
        print("Area of Rectangle={}".format(self.ra))
        print("*"*50)
        super().area()

# Main Program
r=rectangle()
r.area()






