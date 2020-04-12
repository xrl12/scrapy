from threading import Thread,Lock
from time import sleep
lock = Lock()   # 创建一个互斥锁对象
a = 0


def thread1():
    global a
    for i in range(1000000):
        up_lock = lock.acquire(True)  # 上了互斥锁 注意：下面一定接把锁打开 会返回一个布尔型
        if up_lock:
            a += 1
            lock.release()  # 解锁
    print('thread1运行后的结果为{}'.format(a))


def thread2():
    global a
    for i in range(1000000):
        up_lock = lock.acquire(True)  # 上了互斥锁 注意：下面一定接把锁打开
        if up_lock:
            a += 1
            lock.release()  # 解锁
    print('thread2运行后的结果为{}'.format(a))



if __name__ == '__main__':
    print('--------------初始的值:{}--------------'.format(a))
    thread1 = Thread(target=thread1)
    thread1.start()
    thread2 = Thread(target=thread2)
    thread2.start()
    thread2.join(100)
    # thread1.join(100)
    print('--------------结束后:{}--------------'.format(a))



# from threading import Thread, Lock
# import time
#
# g_num = 0
#
#
# def test1():
#     global g_num
#     for i in range(1000000):
#         #True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这里一直等待到解锁为止
#         #False表示非堵塞，即不管本次调用能够成功上锁，都不会卡在这,而是继续执行下面的代码
#         mutexFlag = mutex.acquire(True)
#         if mutexFlag:
#             g_num += 1
#             mutex.release()
#     print("---test1---g_num=%d"%g_num)
#
#
# def test2():
#     global g_num
#     for i in range(1000000):
#         mutexFlag = mutex.acquire(True) #True表示堵塞
#         if mutexFlag:
#             g_num += 1
#             mutex.release()
#     print("---test2---g_num=%d"%g_num)
#
# #创建一个互斥锁
# #这个所默认是未上锁的状态
# mutex = Lock()
#
#
# p1 = Thread(target=test1)
# p1.start()
#
#
# p2 = Thread(target=test2)
# p2.start()
#
# print("---g_num=%d---"%g_num)