# CsvDictWriteEx1.py
# Program for creating csv file by using csv module.
import csv
colnames=["BID","BNAME","BPRISE","BPUBLISHER"]
records=[{"BID":100,"BNAME":"PYTHON","BPRISE":500,"BPUBLISHER":"Rossum"},
         {"BID":200,"BNAME":"JAVA","BPRISE":350,"BPUBLISHER":"James Gosling"},
         {"BID":300,"BNAME":"NUMPY","BPRISE":400,"BPUBLISHER":"Travis"}]  # Dict In List
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\book.csv","w") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=colnames)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created With Dict Objects---Verify!!!")






