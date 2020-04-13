'''
单核cpu下一个进程可以有很多线程 python 不能使用多核多线程
线程是进程的子集
进程：运行中的程序叫进程   多进程信息共享成本很大 所有就有了线程
线程：实现信息共享
同种线程    做一种事情
不同种线程  做不同的事情
'''

import threading
import time

'''
并发
mport threading
import time


def helloworld():   #主线程i
    time.sleep(2)
    print("helloworld")


t = threading.Thread(target=helloworld)  # 新增一个线程 t
t.start()
print("main thread")

# 带参数的并发函数

def helloworld(id):
    time.sleep(2)
    print("thread %d helloworld" % id)


for i in range(5):
    t = threading.Thread(target=helloworld, args=(i,))
    t.start()
print("main thread")

# 例子
import threading
import time
from urllib import request


def get():
    url = "https://jd.com"
    r = request.urlopen(url)
    print(r.code)


for i in range(20):
    t = threading.Thread(target=get)
    t.start()
'''
# 线程间同步
import threading, time

count = 0


def adder():
    global count
    # addlock.acquire()     #  加锁
    # count = count + 1
    # time.sleep(0.1)
    # count = count + 1
    # addlock.release()     #  解锁
    with addlock:           #  使用with加锁  自动解锁，避免遗忘解锁
        count = count + 1
        time.sleep(0.1)
        count = count + 1
#  加锁  只能被一个线程锁定使用，其他线程到这部分就得等着排队，解锁后才能进行之后的线程
addlock = threading.Lock()   #  定义一个addlock的变量
threads = []
for i in range(100):
    thread = threading.Thread(target=adder)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(count)
