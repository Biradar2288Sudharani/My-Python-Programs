# FileWriteEx1.py
with open ("stud.data","w") as fp:
    fp.write(str(30)+"\t")
    fp.write("sm"+"\t")
    fp.write(str(3.24)+"\n")
    print("Data Written To The File.")
with open ("stud.data","a") as fp:
    fp.write(str(40)+"\t")
    fp.write("sudha"+"\t")
    fp.write(str(3.14)+"\n")
    print("Data Written To The File.")









