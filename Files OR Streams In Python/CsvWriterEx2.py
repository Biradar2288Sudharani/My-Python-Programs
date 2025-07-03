# CsvWriterEx2.py-----csv.writer()
# Program for adding new records to csv file to the existing csv file.
import csv
try:
    rec=[16,"suman",8878767862,"IT",766]
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","a") as fp:
        csvwr=csv.writer(fp)
        csvwr.writerow(rec)
        print("New record added to csv file---verify!!!")
except PermissionError:
    print("Permission Denied Please Check It!!!")











