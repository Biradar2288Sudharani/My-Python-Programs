# ActiveCountThreadEx.py
import threading
t=threading.current_thread()
print("Thread Name:",t.name)
noth=threading.active_count()
print("Number of Threads Running",noth)