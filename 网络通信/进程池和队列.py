from queue import Queue
from multiprocessing import Pool,Manager
import os,time

def writeQuque(q,msg):
    print('我正在往队列里面加入数据,我的id是{}，我的父id是{}'.format(os.getpid(),os.getppid()))
    q.put(msg)

def getQueue(q):
    print('我正在网从队列里面取数据,我的di是{}，我的父id是{}'.format(os.getpid(),os.getppid()))
    return q.get()

if __name__ == '__main__':
    pool = Pool()
    q = Manager().Queue() # 创建一个管理队列对象
    for i in range(10):
        pool.apply(func=writeQuque,args=(q,i)) # 使用非堵塞的方法
    for size in range(q.qsize()):
        value = pool.apply(func=getQueue,args=(q,))
        print(value)
    pool.close()
    pool.join()

