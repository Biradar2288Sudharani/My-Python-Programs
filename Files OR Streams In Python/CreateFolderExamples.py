# CreateFolderExamples.py
# mkdir is only one folder created.

# Example 1
'''
import os
os.mkdir("sudha")
print("Folder Created Successfully!!!")
'''

# Example 2
import os
try:
    os.mkdir("sudha")
    print("Folder Created Successfully!!!") 
except FileExistsError:
    print("File is already exist--Please create a new file!!!")


# Example 3
import os
try:
    os.mkdir("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\sudha\\python")
    print("Folder Created Successfully!!!") 
except FileExistsError:
    print("File is already exist--Please create a new file!!!")


# Example 3
import os
try:
    os.mkdir("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\bok.csv")
    print("Folder Created Successfully!!!")
except FileExistsError:
    print("File is already exist!!!")
except FileNotFoundError:
    print("Previous folder does not find!!!")


# ----> Create Folder Heirarchy (Here heirarchy means multiple)<----
# Example 4
'''
import os
os.makedirs("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\\banana\\orange\\greaps")
print("Folders Heirarchy Created ---- Verify!!!")
'''

# Example 5
import os
try:

    os.makedirs("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\apple\\mango\\banana\\orange\\greaps")
    print("Folders Heirarchy Created ---- Verify!!!")

except FileExistsError:
    print("File is already exist !!")












