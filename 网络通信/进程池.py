from multiprocessing import Pool
import time
import random
import os

"""

当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，
此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，
那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行，请看下面的实例
"""
def workon(i):
    start_time = time.time()
    print('{}进程正在运行{}'.format(i,os.getpid()))
    sleep_time = random.random()*2
    time.sleep(sleep_time)
    end_time = time.time()
    print('{}进程结束完了，共耗时为{}'.format(os.getpid(),end_time-start_time))



pools = Pool(3) # 表示最多可以创建3个进程
for i in range(10):
    pools.apply_async(func=workon,args=(i,)) # 使用堵塞方法进行创建 使用args进行传参
    # pools.apply(func=workon,kwds={'i':i}) # 使用堵塞方法进行创建 使用kwargs进程传参

pools.close()  # 关闭Pool，使其不再接受新的任务；
pools.join()  # 主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；
pools.terminate()  # 不管任务是否完成，立即终止；





# pools = Pool(3) # 表示最多可以创建3个进程
# for i in range(10):
#     # pools.apply_async(func=workon,args=(i,)) # 使用非堵塞方法进行创建 使用args进行传参
#     pools.apply_async(func=workon,kwds={'i':i}) # 使用非堵塞方法进行创建 使用kwargs进程传参
#
# pools.close() # 关闭Pool，使其不再接受新的任务；
# pools.join() # 主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；
# pools.terminate() # 不管任务是否完成，立即终止；