# IsAliveEx.py
import threading
class hyd:
    def welcome(self,val):
        print("Thread Name:{} executing welcome()".format(threading.current_thread().name))
        print("Hi,{} , Good Morning".format(val))
        print("*"*50)
# Main Program
# create sub thread
t1=threading.Thread(target=hyd().welcome,args=("KVR",)) # here t1 is call subthread object whose deafult name is "thread-1"
t1.name="KVR"
print("Is t1 sub executing before start() ?=",t1.is_alive)
t1.start()
print("Is t1 sub executing after start() ?=",t1.is_alive)
