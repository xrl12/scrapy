from threading import Thread
import threading
import time

def saySorry(a):
    print('threading.current_thread',threading.current_thread())   # 获取当前线程的详细信息
    print('currentThread'.format(threading.currentThread()))
    print('你好啊，猜猜我是谁{}'.format(a))
    time.sleep(1)

if __name__ == '__main__':
    for i in range(10):
        thread = Thread(target=saySorry,args=(i,))
        thread.start()
    thread.setName('你猜')
    name = thread.getName()
    print(name)
    thread.join(3)
    print('进程结束了')
    print(thread.is_alive())
    print(thread.getName())