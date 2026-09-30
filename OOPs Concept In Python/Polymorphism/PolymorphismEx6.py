# PolymorphismEx6.py

class circle(object):  
    def area(self,r):  # Original Method
        self.ac=3.14*r**2
        print("Area Of Circle={}".format(self.ac))

class square(circle):  
    def area(self,s):  # Overriden Method
        self.sa=s*s
        print("Area Of Square={}".format(self.sa))
        
class rectangle(square):  
    def area(self,l,b):  # Overriden Method
        self.ar=l*b
        print("Area Of Rectangle={}".format(self.ar))
        print("*"*50)
        square().area(self,2)
        circle().area(self,7)

# Main Program
r=rectangle()
r.area(3,5)






