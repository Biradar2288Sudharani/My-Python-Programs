# CsvWriterEx1.py-----csv.write()
# Program for creating CSV File by using CSV Module.

import csv
try:
    # Step-1: Take Header Names or Column Names
    colnames=["ENO","ENAME","SAL","DSG"]

    # Step-2: Take Records---always in the form of lists in list.
    records=[[10, "tushar", 4567890123, "E&TC", 456],
            [11, "srushti", 5678901234, "CSE",567],
            [12, "pratiksha", 5678901234, "CSE",465],
            [13, "sarthak", 7890123456, "CIVIL", 789]]  # Lists IN List

    # Step-3: Choose the filename and open in write mode
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Student.csv","w") as fp:
        csvwr=csv.writer(fp) # Here csvr is an object of <class,'csv.writer'>

        # Step-4: Write Header Name
        csvwr.writerow(colnames)

        # Step-5: Write Records
        csvwr.writerows(records)

        print("CSV File Created Verify!!!")

except PermissionError:
    print("Permission Denied Please Check It!!!")












