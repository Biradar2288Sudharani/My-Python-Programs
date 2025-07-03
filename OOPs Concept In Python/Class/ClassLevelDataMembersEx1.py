# ClassLevelDataMembersEx1.py
# For demonstrating class level data members.
class student:
    crs="PYTHON"   # Here crs is called class level data members.
# Main Program
s1=student()
s2=student()
print("Initial Content of s1=",s1.__dict__)
print("Initial Content of s2=",s2.__dict__)
print("First Student s1 Course=",student.crs)
print("First Student s2 Course=",student.crs)

# Here we are accepting class level data members w.r.t class name.














