# CurrentThreadEx.py
import threading
t=threading.current_thread()
print("Thread Name:",t.name) #main thread
print("---OR---")
print("Thread Name:",threading.current_thread().name) # main thread