# FileImageCopyEx.py
# WAPP which will copy one image from one file to another file.
try:
    with open ("C:\\Users\\lenovo\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\kvr.png","rb") as rp:
        with open ("photo.png","ab") as wp:
            srcfiledata=rp.read()
            wp.write(srcfiledata)
            print("Source file image copied into destination file---verify!!!")

except FileNotFoundError:
    print("Source File Doesn't Exist.")              

















