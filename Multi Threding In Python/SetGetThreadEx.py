# SetGetThreadEx.py
# SetName()---> Deprecated on the name of the "name"
# GetName()---> Deprecated on the name of the "name"
import threading
class hyd:
    def welcome(self,val):
        print("Thread Name:{} executing welcome()".format(threading.current_thread().name))
        print("Hi,{} , Good Morning".format(val))
        print("*"*50)
# creat sub thread for concurrency 
t1=threading.Thread(target=hyd().welcome,args=("KVR",)) # here t1 is call subthread object whose deafult name is "thread-1"
# get the name of the sub thread
# stname=t1.gtname() -> here getname Deprecated on the name of the "name" attribute
stname=t1.name
print("Default Name of sub thread before setting=",stname)
# set the user friendly name to the sub thread
# t1.setname=("KVR") -> here setname(str) Deprecated on the name of the "name" attribute
t1.name="KVR"
# get the name of the subthrea after setting
stname=t1.name
print("Default name of sub thread after setting =",stname)

