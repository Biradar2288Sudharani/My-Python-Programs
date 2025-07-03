# FileWriteEx2.py

# Example 1
x=[10,"RS",3.14,True]
with open ("stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written To The File")


# Example 2
x=[20,"SB",3.15,False]
with open ("stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written To The File")


# Example 3
x={10,20,10,30,20,40,30,10}
with open ("stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written To The File")








