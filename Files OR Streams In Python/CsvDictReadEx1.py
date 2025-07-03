# CsvDictReadEx1.py-----csv.DictReader()
# Program for reading the data from CSV Files---by using CSV module in the form of dict.

# Logic 1
import csv
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","r") as fp:
    csvdr=csv.DictReader(fp) # Here csvr is an object of <class,'csv.DictReader'>
    for record in csvdr: # Here csvdr is an object of <class,'dict'>
        print(record)

# Logic 2
import csv
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","r") as fp:
    csvdr=csv.DictReader(fp) # Here csvr is an object of <class,'csv.DictReader'>
    for record in csvdr: # Here csvdr is an object of <class,'dict'>
        for k,v in record.items():
            print("\t{}-->{}".format(k,v))
        print("*"*100)
        
# Logic 3
import csv
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","r") as fp:
    csvdr=csv.DictReader(fp) # Here csvr is an object of <class,'csv.DictReader'>
    i=1
    for record in csvdr:
        print("\t\t{} Record".format(i))
        print("*"*100)
        for k,v in record.items():
            print("\t{}-->{}".format(k,v))
        print("*"*100)
        i=i+1
        




