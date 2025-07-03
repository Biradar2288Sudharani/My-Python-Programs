# program for generating different multables by different threads by using threads
#SynchOopsEx3.py
import threading , time
class Table:
    def __init__(self,n):
        self.n=n
    def multable(self):
        L.acquire()  #Step2
        if(self.n<=0):
            print("{}-->{} Is Invalid Input".format(threading.current_thread().name,self.n))
        else:
            print("*"*50)
            print("Mul Table for {}".format(self.n))
            print("*"*50)
            for i in range(1,11):
                print("\t{}->{} x {}={}".format(threading.current_thread().name,self.n,i,self.n*i))
                time.sleep(1)
            else:
                print("*"*50)
        L.release()  #Step3
# Main Program
L=threading.Lock()  #create an object of lock class-->step1
# create multiple threads targeting single function
t1=threading.Thread(target=Table(int(input("Enter a number for generating a multable for Thread 1"))).multable)
t2=threading.Thread(target=Table(int(input("Enter a number for generating a multable for Thread 2"))).multable)
t3=threading.Thread(target=Table(int(input("Enter a number for generating a multable for Thread 3"))).multable)
t4=threading.Thread(target=Table(int(input("Enter a number for generating a multable for Thread 4"))).multable)
# Dispatch all sub threads
t1.start()
t2.start()
t3.start()
t4.start()




