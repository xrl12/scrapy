from threading import Thread
import os

def workon(a,b):
    pid = os.getppid()
    print(pid)
    print('你好啊'+a+b)


thread = Thread(target=workon,args=('1','2'))
thread.start()
