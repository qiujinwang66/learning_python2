from multiprocessing import Pool
import time


def func(num):
    print("hello world %d" % num)
    time.sleep(3)


if __name__ == '__main__':

    pool = Pool(processes=4)  # 4个进程执行一次
    pool.map(func, range(10))  # pool.map这个方法默认是异步执行
    #for i in range(10):
    #    pool.apply_async(func, (i,))  #  异步执行  （apply是同步执行）
    pool.close()
    pool.join()

'''
from multiprocessing import Pool
import time
def f(x):
    time.sleep(0.5)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, range(10)))

'''