# NonCsvReadEx1.py
# Program for reading the data from CSV Files---by using file pointer which is an object TextIOPointer.
import csv
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","r") as fp:
    csvr=csv.reader(fp) # Here csvr is an object of <class,'csv.reader'>
    for record in csvr:
        for value in record:
            print("{}".format(value),end="\t")
        print() 










