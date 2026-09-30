# DeleteRemoveFolderExamples.py
# Program for deleting folder at a time.

# Example 1
'''
import os
os.rmdir("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\banana\\orange\\greaps")
print("Folder Deleted Successfully!!!")
'''

# Example 2
import os
try:
    os.rmdir("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\banana\\orange\\greaps")
    print("Folder Deleted Successfully!!!")
except OSError:
    print("Folder is not empty!!!")


# ----> Delete or Remove Folder Heirarchy (Here heirarchy means multiple)<----
# Example 3
import os
os.removedirs("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\\banana\\orange\\greaps")
print("Folder Deleted Successfully!!")

# Exampl 4
import os
try:
    os.removedirs("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\banana\\orange\\greaps")
    print("Folder Deleted Successfully!!!")
except OSError:
    print("Folder is not empty!!!")
except FileNotFoundError:
    print("Folder not shown!!!")
 