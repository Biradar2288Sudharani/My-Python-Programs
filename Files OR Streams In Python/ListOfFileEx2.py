# ListOfFileEx2.py
# Program for listing the file or display the file names in folder.
import os
try:
    foldername=input("Enter Folder Name:")
    FileNames=os.listdir(foldername) # Here FileNames is an object of listtype.
    print("*"*50)
    print("List Of Files")
    print("*"*50)
    for filename in FileNames:
        print("\t\t{}".format(filename))
    print("*"*50)
    print("Number Of File={}".format(len(FileNames)))
except FileNotFoundError:
    print("Folder Doesn't Exist!!!")



''' ---> ANSWER <---
Enter Folder Name:Files OR Streams In Python
**************************************************
List Of Files
**************************************************
                .idea
                bok.csv
                book.csv
                ContentReadEx.py
                CreateFolderExamples.py
                CsvDictReadEx1.py
                CsvDictReadEx2.py
                CsvDictWriteEx1.py
                CsvReadEx1.py
                CsvWriterEx1.py
                CsvWriterEx2.py
                DeleteFileExamples.py
                DeleteRemoveFolderExamples.py
                Employee.data
                EmpPickEx1.py
                EmpPickEx2.py
                EmpUnPickEx1.py
                EmpUnPickEx2.py
                EOFErrorEx.py
                FileCopyEx1.py
                FileImageCopyEx.py
                FileNameCountEx.py
                FileOpenEx1.py
                FileOpenEx2.py
                FileOpenEx3.py
                FileOpenEx4.py
                FileOpenEx5.py
                FileOpenEx6.py
                FileOpenEx7.py
                FileOpenEx8.py
                FileReadEx1.py
                FileReadEx2.py
                FileReadEx3.py
                FileReadEx4.py
                FileWriteEx1.py
                FileWriteEx2.py
                GetVowelEx.py
                KVR.data
                kvr.png
                kvr1.py
                kvr2.py
                ListOfFileEx1.py
                ListOfFileEx2.py
                NonCsvReadEx.py
                photo.png
                RandomAccessEx.py
                RenameingFolderExamples.py
                RenamingFileExamples.py
                St.txt
                stud1.data
                StudDetailsEx.py
                Student.csv
                student.data
                StudentDetailsEx.py
                StudentDetailsEx2.py
                StudentRecordsEx.py
                sudha.data
                sudharani
**************************************************
Number Of File=58
'''








