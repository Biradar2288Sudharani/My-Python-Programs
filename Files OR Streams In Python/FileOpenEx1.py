# FileOpenReadEx1.py

fp=open("KVR.data","r")
print("File opened in read mode successfully.")
print("*"*50)

try:
    fp=open("KVR.data","r")
    print("File opened in read mode successfully.")
    
except FileNotFoundError:
    print("File Does Not Exist!")
















