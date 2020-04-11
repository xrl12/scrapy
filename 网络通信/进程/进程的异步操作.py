from multiprocessing import Pool
from time import sleep
import os


def test1():
    print('我的进程号是{}'.format(os.getpid()))
    for i in range(3):
        print(i)
        sleep(1)
    return '臭弟弟'


def test2(args):
    print('backfun-----pid'.format(os.getpid()))
    print('backfun------args'.format(args))


if __name__ == '__main__':
    pools = Pool()
    pools.apply_async(func=test1,callback=test2)  #callback表示回调函数,会把test1返回的值传给test2
    pools.close()  # 关闭Pool，使其不再接受新的任务；
    pools.join()
