import os
for i in range (0,6):
    pid = os.fork()

# 如果os.fork()的返回值是0时，则就是一个子进程，
# 如果是父进程就会返回这个子进程的进程号

print(os.getpgid(pid))  # 获取当前父进程下面子进程的进程号
print(os.getppid()) # 获取当前父进程的进程号
if pid == 0:
    print('我是子进程')
else:
    print('我是父进程')
