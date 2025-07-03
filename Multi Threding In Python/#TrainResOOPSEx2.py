#TrainResFunEx1.py
import threading , time
class Train:
    K=threading.Lock()
    totseats=15  # global keyword
    def reservation(nos):
        Train.K.acquire()
        global totseats
        if(nos>Train.totseats):
            print("\t Hi {},{} Seats are not available--Try Next!". format(threading.current_thread().name,nos))
            time.sleep(1)
        else:
            Train.totseats=Train.totseats-nos
            print("\t Hi {},{} Seats are available--Happy Journey !". format(threading.current_thread().name,nos))
            time.sleep(1)
            print("\t Now available seats={}".format(Train.totseats))
            time.sleep(1)
            if(Train.totseats==0):
                print("\t Train Is Full")
            print("*"*50)
        Train.K.release()
# Main Program
t1=threading.Thread(target=Train.reservation, args=(10,))
t1.name="Sudha"
t2=threading.Thread(target=Train.reservation, args=(5,))
t2.name="Shankar"
t3=threading.Thread(target=Train.reservation, args=(7,))
t3.name="Sudharani"
# dispatch all sub threads
t1.start()
t2.start()
t3.start() 