from threading import Thread
import os
class MyThread(Thread):

    def __init__(self):
        super().__init__()  # 当从写init方法的时候，需要调用一下父类的init方法

    def sing(self):
        print('{}正在唱一首好听的歌曲'.format(self.name))

    def run(self):
        # 重写run方法
        print('run方法正在启动{}'.format(os.getpid()))
        self.sing()
        super(MyThread, self).run()

if __name__ == '__main__':
    for i in range(1,6):
        mythread = MyThread()
        mythread.start()
