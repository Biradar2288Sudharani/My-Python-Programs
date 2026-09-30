# Program for demonstrating how main thread execute all the functions in program without creating sub treads
# DefaultThread ExecutionProcessWithoutSubThreads.py
import threading, time
def square(lst):
    for val in lst:
        print("{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
def cube(lst):
    for val in lst:
        print("{}-->Cube({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)
# Main Program
bt=time.time()
print("*"*50)
print("Line 15-> Executed By:",threading.current_thread().name)
print("*"*50)
lst=[3,12,-5,14,25,-3,7]
square(lst)
print("*"*50)
cube(lst)
print("*"*50)
et=time.time()
print("Execution of this program without threads ={}".format(et-bt))
# ANS:- Execution of this program without threads =14.05141830444336