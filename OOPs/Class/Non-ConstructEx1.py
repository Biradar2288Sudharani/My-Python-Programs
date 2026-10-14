# Non-ConstructEx1.py
# Program for demonstrating need for constructor.
class student:
    def readstudvalues(self):
        self.sno=10
        self.sname="sudha"

# Main Program
s=student()
print("Content of s=",s.__dict__)  # Content of s= {}
  
# Place the instance data in object s
s.readstudvalues()  # Calling instance method explicitely
print("Content of s=",s.__dict__)  # {'sno':10, 'sname':'sudha'}









