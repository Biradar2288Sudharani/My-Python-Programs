# CsvDictWriteEx2.py------csv.DictReader()
import csv
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\book.csv","r") as fp:
    csvdr=csv.DictReader(fp)
    i=1
    for record in csvdr:
        print("\t\t{} Book Record".format(i))
        print("*"*50)
        for k,v in record.items():
            print("\t{}-->{}".format(k,v))
        print("*"*50)
        i=i+1























