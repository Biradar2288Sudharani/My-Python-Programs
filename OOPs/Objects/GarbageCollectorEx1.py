# GarbageCollectorEx1.py
# Program for demonstrating Garbage Collector running or not.
import gc
print("Program Execution Started")
print("\t Initially , Is Garbage Collector Running=",gc.isenabled())  # True
a=10
b=20
gc.disable()
print("Val of a=",a)
print("Val of a=",a)
print("\t Now Is Garbage Collector Running after disable()=",gc.isenabled)  # False
c=a+b
gc.enable()
print("Sum=",c)
print("\t Now is running after enable()=",gc.isenabled())  # True
print("Program Execution Started!!!")


