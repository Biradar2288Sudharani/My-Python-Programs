# This is Object Oriented programing example
# ThreadCreationEx4.py
import threading
class hyd:
    def welcome(self,val):
        print("Thread Name:{} executing welcome()y".format(threading.current_thread().name))
        print("Hi,{} , Good Morning".format(val))
        print("*"*50)

class bang:
    def great(self):
        print("*"*50)
        print("Thread Name:{} executing great()".format(threading.current_thread().name))
        print("Hi,to all read python notes well")
        print("*"*50)

# Main Program
tname=threading.current_thread().name
print("Main Program->Default Thread Name:",tname)
# creat sub thread for concurrency 
t1=threading.Thread(target=hyd().welcome,args=("KVR",))# here t1 is call subthread object whose deafult name is "thread-1"
t2=threading.Thread(target=bang().great)# here t2 is call subthread object whose deafult name is "thread-2"
print("Number of Threads in this program=",threading.active_count())
# Dispatch the sub threads
t1.start()
t2.start()

