# InstanceDataMembersEx1.py
# Program for demonstrating instance data members. 
class student:pass
# Main Program
s1=student()  # Object Creation
s2=student()  # Object Creation
print("#"*50)
print("ID of s1={}".format(id(s1)))
print("ID of s2={}".format(id(s2)))
print("*"*50)

# Add instance data members to object s1-through.
s1.sno=100
s1.name="sudha"
s1.marks=87.43    # Here sno,name and marks are called instance data members.

# Add instance data members to object s2-through.
s2.sid=100
s2.name="suhas"
s2.marks=77.45

print(" -----> First Student Information <----- ")
print("*"*50)
print("Student Number={}".format(s1.sno))
print("Student Name={}".format(s1.name))
print("Student Marks={}".format(s1.marks))
# Here we are accessing instance data members by using object name.

print("*"*50)
print(" -----> Second Student Information <----- ")
print("*"*50)
print("Student ID={}".format(s2.sid))
print("Student Name={}".format(s2.name))
print("Student Marks={}".format(s2.marks))
print("#"*50)
# Here we are accessing instance data members by using object name.





