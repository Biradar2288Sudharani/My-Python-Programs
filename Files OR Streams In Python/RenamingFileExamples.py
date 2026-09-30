# RenamingFileExamples.py
# Program for renaming the file.

# Example 1
import os
try:
    os.rename("stud.data","sudha.data")
    print("File name is renamed verify!!!")
except FileNotFoundError:
    print("Source file name does not exist!")
except FileExistsError:
    print("Destination file name, are already exist!")







