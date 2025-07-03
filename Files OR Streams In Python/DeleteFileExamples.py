# DeleteFileExamples.py
# Program for removing the file.

# Example 1
import os
os.remove("amma.data")
print("File Removed Verify!!!")

# Example 2
import os
try:
    os.remove("amma.data")
    print("File Removed Verify!!!")
except FileNotFoundError:
    print("File name doesn't exist!!")



