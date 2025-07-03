# Program for demonstrating how main thread execute all the functions in program with creating sub treads
# ThreadExecutionWithSubTreads.py
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
t1=threading.Thread(target=square,args=(lst,)) # sub Tread Creation 1
t2=threading.Thread(target=cube,args=(lst,)) # sub Tread Creation 2
print("*"*50)
t1.start()
t2.start()
print("*"*50)
t1.join()
t2.join()
et=time.time()
print("Execution of this program with threads ={}".format(et-bt))
# ANS:- Execution of this program with threads =7.03585958480835