from os import fork,getpid,getppid

# pid = fork()
#
# #  getpid 是获取当前线程的id，如果是主进程就是主进程的id，如果是子进程就是子进程的id
# #  getppid 获取当前进程的父进程的id
# #  全局变量在使用的过程中，主进程和子进程是每个进程一个，两个变量互不干涉
# if pid<0:
#     print('fork调用失败')
# elif pid == 0:
#     print('我是子进程{},我的父进程的id是{}'.format(getpid(),getppid()))
# else:
#     print('我的父进程{},我的子进程的id是{}'.format(getpid(), pid))
#


pid = fork()

num = 10

if pid == 0:
    num += 20
    print('我是子进程---num={}'.format(num))
else:
    num += 1
    print('我是父进程---num={}'.format(num))

