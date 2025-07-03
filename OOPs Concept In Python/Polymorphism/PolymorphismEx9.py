# PolymorphismEx9.py

class circle:  
    def __init__(self):  # Original Constructor
        print("Drawing Circle")

class square(circle):
    def __init__(self):  # Overriden Constructor
        print("Drawing Square")

class rectangle(square):
    def __init__(self):  # Overriden Constructor
        print("Drawing Rectangle")
        circle.__init__(self)
        square.__init__(self)
               
# Main Program
r=rectangle()     # Object Creation













