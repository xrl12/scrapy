from multiprocessing import Process
import os

def workon(age):
    print('我里面的参数是{},我的id号{},我父亲的id是{}'.format(age,os.getpid(),os.getppid()))

for i in range(1,2):
    proces = Process(target=workon, args=(11,), name=i)
    proces.start()  # 里面会自动调用run方法
    print(proces.name)  # 查看这个进程的别名，如果不存在就是返回一个proces+负数
    print(proces.is_alive())  # 查看是否还存在
