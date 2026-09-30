# EOFErrorEx.py
import pickle
def reademprecords():
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\KVR Lecture Program\\Files OR Streams In Python\\Employee.data","rb") as fp:
        emprec=pickle.load(fp)
        print(emprec,type(emprec))
        emprec=pickle.load(fp)
        print(emprec,type(emprec))
        emprec=pickle.load(fp)
        print(emprec,type(emprec))
        emprec=pickle.load(fp)
        print(emprec,type(emprec))
        emprec=pickle.load(fp)
        print(emprec,type(emprec))
        emprec=pickle.load(fp)
        print(emprec,type(emprec))

# Main Program
reademprecords()


# EOFError: Ran out of input








