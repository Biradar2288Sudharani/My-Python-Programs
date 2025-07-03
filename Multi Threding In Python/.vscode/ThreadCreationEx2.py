# This is Object Oriented programing example
# ThreadCreationEx2.py
import threading
class hyd:
    def welcome(self,val):
        print("Thread Name:{} executing welcome()".format(threading.current_thread().name))
        print("Hi,{} , Good Morning".format(val))
        print("*"*50)

    def great(self):
        print("*"*50)
        print("Thread Name:{} executing great()".format(threading.current_thread().name))
        print("Hi,to all read python notes well")
        print("*"*50)

# Main Program
tname=threading.current_thread().name
print("Main Program->Default Thread Name:",tname)
h=hyd()
# creat sub thread for concurrency 
t1=threading.Thread(target=h.welcome,args=("KVR",))# here t1 is call subthread object whose deafult name is "thread-1"
t2=threading.Thread(target=h.great)# here t2 is call subthread object whose deafult name is "thread-2"
print("Number of Threads in this program=",threading.active_count())
# Dispatch the sub threads
t1.start()
t2.start()
print("Number of threads in this program=",threading.active_count())
