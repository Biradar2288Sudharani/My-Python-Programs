# program for generating different multables by different threads by using threads
#SynchOopsEx2.py
import threading , time
class Table:
    def multable(self,n):
        L.acquire()  #Step2
        if(n<=0):
            print("{}-->{} Is Invalid Input".format(threading.current_thread().name,n))
        else:
            print("*"*50)
            print("Mul Table for {}".format(n))
            print("*"*50)
            for i in range(1,11):
                print("\t{}->{} x {}={}".format(threading.current_thread().name,n,i,n*i))
                time.sleep(1)
            else:
                print("*"*50)
        L.release()  #Step3
# Main Program
L=threading.Lock()  #create an object of lock class-->step1
# create multiple threads targeting single function
t1=threading.Thread(target=Table().multable,args=(int(input("Enter a number for generating a multable for Thread 1")),))
t2=threading.Thread(target=Table().multable,args=(int(input("Enter a number for generating a multable for Thread 2")),))
t3=threading.Thread(target=Table().multable,args=(int(input("Enter a number for generating a multable for Thread 3")),))
t4=threading.Thread(target=Table().multable,args=(int(input("Enter a number for generating a multable for Thread 4")),))
# Dispatch all sub threads
t1.start()
t2.start()
t3.start()
t4.start()




