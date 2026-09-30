# DefaultParameterizedContructEx1.py
# Program for demonstraying both default and parameterized constructor.
class test:
    def __init__(self,k=1,v=2):
        print("I am from both default and parameterized constructor. ")
        self.a=k
        self.b=v
        print("\t a={} \t b={}".format(self.a,self.b))

# Main Program
t1=test()  # Object creation calls default and parameterized constructor.
t2=test()  # Object creation calls default and parameterized constructor.








