from threading import Thread,Lock
import time
"""
什么是死锁：在现场中，如果线程同时共享一部分资源，并且都在等对方释放资源就会造成死锁
如何避免死锁： 可以添加一个超时时间
"""


class MyThread1(Thread):
    def run(self):
        if thread1.acquire(blocking=True,timeout=2):  # 给thread1进行上锁
            print(self.name,'我是锁一')
            time.sleep(1)
            if thread2.acquire(blocking=True,timeout=2):
                print(self.name,'我是锁二')
                time.sleep(1)
                thread1.release()  # 解锁thread1
            thread2.release()  # 解锁thread2

class MyThread2(Thread):
    def run(self):
        if thread2.acquire(blocking=True,timeout=2):
            print(self.name,'我是锁二')
            time.sleep(1)
            if thread1.acquire(blocking=True,timeout=2):
                print('{}我是锁一'.format(self.name))
                time.sleep(1)
                thread2.release()
            thread1.release()



if __name__ == '__main__':

    thread1 = Lock()
    thread2 = Lock()
    my_thread1 = MyThread1()
    my_thread2 = MyThread2()
    my_thread1.start()
    my_thread2.start()

