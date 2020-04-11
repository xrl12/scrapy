from threading import Thread,Lock
import time

class MyThread1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('我正在执行锁一')
                time.sleep(1)
                lock2.release()
class MyThread2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('我正在执行锁二')
                time.sleep(1)
                lock3.release()

class MyThread3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('我正在锁三')
                time.sleep(1)
                lock1.release()





if __name__ == '__main__':

    lock1 = Lock()

    lock2 = Lock()
    lock2.acquire()

    lock3 = Lock()
    lock3.acquire()

    thread1 = MyThread1()
    thread1.start()

    thread2 = MyThread2()
    thread2.start()

    thread3 = MyThread3()
    thread3.start()