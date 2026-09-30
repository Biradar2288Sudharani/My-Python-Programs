# StudentDetailsEx2.py
# WAPP which will accept any type of data and save or write to the file until we press some symbol (@).
# program for reading the data from keyboard and write it to the file.
with open("C:\Python-9am\hyd.info","a") as fp:
    print(" Enter the Information from keyboard for writing it to the file.")
    while(True):
        data=input()
        if(data=="@"):
            print("\n Data written to the file----verify!!")
            break
        else:
            fp.write(data+"\n")
            
           







