# DefaultConstructEx1.py
# Program for demonstrating default constructor.
class test:
    def __init__(self):
        print("I am from default constructor")
        self.a=10
        self.b=20
        print("\t a={} \t b={}".format(self.a,self.b))

# Main Program
t1=test()  # Object creation calls default constructor.
t2=test()  # Object creation calls default constructor.
t3=test()  # Object creation calls default constructor.


