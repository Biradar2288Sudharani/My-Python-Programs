# FileOpenWriteEx2.py
fp=open("KVR.data","w")
print("File opened in write mode successfully.")
print("Type of fp=",type(fp))
print("*"*50)
try:
    fp=open("KVR.data","w")
    print("File opened in write mode successfully.")
    
except FileNotFoundError:
    print("File Does Not Exist!")