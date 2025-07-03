# Program for demonstrating that there exist single tread
# DefaultTreadNameEx.py
import threading
tname=threading.current_thread().name
print("Default Thread Name=",tname)
print("Number of treads by Default Executing ", threading.active_count())
