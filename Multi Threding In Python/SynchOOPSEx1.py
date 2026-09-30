# program for generating different multables by different threads by using threads
#Non-SynchOopsEx1.py
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
t1=threading.Thread(target=Table().multable,args=(10,))
t2=threading.Thread(target=Table().multable,args=(20,))
t3=threading.Thread(target=Table().multable,args=(15,))
t4=threading.Thread(target=Table().multable,args=(13,))
# Dispatch all sub threads
t1.start()
t2.start()
t3.start()
t4.start()




