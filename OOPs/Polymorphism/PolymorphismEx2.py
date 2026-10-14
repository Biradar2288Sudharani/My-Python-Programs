# PolymorphismEx2.py

# Logic 1
class circle:  
    def draw(self):  # Original Method
        print("Drawing Circle")

class square(circle):
    def draw(self):  # Overriden Method
        print("Drawing Square")
        super().draw()

class rectangle(square):
    def draw(self):  # Overriden Method
        print("Drawing Rectangle")
        super().draw()
        # super is used for calling base class method from derived class method
        
# Main Program
r=rectangle()
r.draw()


# Logic 2
class circle:  
    def draw(self):  # Original Method
        print("Drawing Circle")

class square(circle):
    def draw(self):  # Overriden Method
        print("Drawing Square")

class rectangle(square):
    def draw(self):  # Overriden Method
        print("Drawing Rectangle")
        circle.draw(self)
        square.draw(self)
        
# Main Program
r=rectangle()
r.draw()

















