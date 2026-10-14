# ParameterizedConstructEx1.py
# Program for demonstrating Parameterized constructor.
class test:
    def __init__(self,k,v):
        print("I am from default constructor")
        self.a=k
        self.b=v
        print("\t a={} \t b={}".format(self.a,self.b))

# Main Program
t1=test(10,20)  # Object creation calls Parameterized constructor.
t2=test(100,200)  # Object creation calls Parameterized constructor.
t3=test(1000,2000)  # Object creation calls Parameterized constructor.




