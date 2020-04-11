from threading import Thread
from time import sleep

"""
进程是系统分配资源的基本单位
线程是系统调度的基本单位
这些全局变变量是必须在一个线程里面
线程之间的全局变量是共享的
"""

a = 0

def test():
    global a
    a += 10
    print('这是修改后的值{}'.format(a))

def test1():
    global a
    print('a =',a)


if __name__ == '__main__':
    print('这个是修改前的值')
    thread1 = Thread(target=test)
    thread1.start()
    sleep(1)  # 是为了保证thread1全部执行完
    thread2 = Thread(target=test1)
    thread2.start()

