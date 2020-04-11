from multiprocessing import Queue
import time
queue = Queue(3)  # 表示最多可以存放的消息数
print(queue.empty()) # 查看队列是否为空，如果为空就返回True，不为空返回False
for i in range(1,4):
    print('queue.empty:',queue.empty())
    print('我放进去了')
    print('queue.full:',queue.full()) # 查看队列有没有满，如果满了就返回True，没有就返回False
    queue.put('徐瑞鑫是个大笨蛋{}'.format(i))

print(queue.empty())
print(queue.full())

start = time.time()
size = queue.qsize()  # 表示里面存放的大小
print(size)
try:
    # 第一个参数表示放的消息 第二个表示是否进行等待，第三个表示多长时间 单位是秒
    queue.put('你猜我会不会报错',True,3)
except:
    end = time.time()
    print(end-start)

try:
    queue.put_nowait('你猜我会不会报错')
except:
    # 取出第一个放在队列里面的值
    for i in range(queue.qsize()):
        zhi = queue.get()  # 获取对列中的数据，并从对列中移除 如果队列里面中没有数据，就会一直等一下
        # zhi = queue.get(True,1)  # 获取对列中的数据，并从对列中移除 如果队列里面中没有数据，会抛出一个异常
        queue.put_nowait('你猜我会不会报错')



        print(zhi)

