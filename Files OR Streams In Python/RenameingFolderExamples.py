# RenamingFolderExamples.py
# Program for ranaming a folder.

# Example 1
import os
os.rename("sudha","sudharani")
print("Folder Renamed Verify !!!")


# Example 2
import os
try:
    os.rename("sudha","sudharani")
    print("Folder Renamed Verify !!!")
except FileNotFoundError:
    print("Source folder name does not exist!!!")






