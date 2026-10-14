# InhProgExample1.py

class circle:
    def draw1(self):
        print("Drawing Circle")

class square(circle):
    def draw2(self):
        print("Drawing Square")

class rectangle(square):
    def draw3(self):
        print("Drawing Rectangle")

# Main Program
r=rectangle()
r.draw1()
r.draw2()
r.draw3()












