# PolymorphismEx8.py

class circle:  
    def __init__(self):  # Original Method
        print("Drawing Circle")

class square(circle):
    def __init__(self):  # Overriden Method
        print("Drawing Square")
        super().__init__()

class rectangle(square):
    def __init__(self):  # Overriden Method
        print("Drawing Rectangle")
        square.__init__(self)
               
# Main Program
r=rectangle()     # Object Creation
















