'''
多线程、多进程
1. 使用多线程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码，
2. 使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码，
3. get和post方法的区别
4. post请求有几种数据格式
'''
#  1. 使用多线程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码
import threading, queue
import time
import requests, time, queue

requestnum = 10
datanum = 2
url = "http://www.baidu.com"
lock = threading.Lock()
dataQueue = queue.Queue()


def producer(num):  # 一个生产者生产四条消息  并且加到dataQueue里面
    dataQueue.put(i)  # 加到dataQueue里面


def consumer(num):
    while True:
        try:
            data = dataQueue.get(block=False)  # 消费者去 dataQueue 取值，如果是false 跳出循环  这里如果写true的话就不能自动跳出，就会一直等待生产者生产的东西，卡死了
        except queue.Empty:  # 如果异常报错
            break
        with lock:  # 消费者去 dataQueue 取值，如果有值 就添加到队列中
            r = requests.get(url)
            print(r.status_code)
        time.sleep(1)
        dataQueue.task_done()


if __name__ == "__main__":

    for i in range(requestnum):
        t = threading.Thread(target=producer, args=(i,))
        t.start()

    for i in range(datanum):
        t = threading.Thread(target=consumer, args=(i,))
        t.start()

    dataQueue.join()

#  2. 使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码，


import requests, time, queue
from multiprocessing import Pool


def func(num):
    r = requests.get(url)
    time.sleep(1)
    print(r.status_code)


if __name__ == '__main__':
    url = "http://www.baidu.com"
    pool = Pool(processes=4)  # 4个进程执行一次
    pool.map(func, range(10))  # pool.map这个方法默认是异步执行
    pool.close()
    pool.join()
#   3.  get和post方法的区别
'''
区别一:语义上的区别

1、Get向服务器请求数据。依照HTTP协议，get 是用来请求数据。

2、Post向服务器发数据。依照HTTP协议，Post的语义是向服务器添加数据，也就是说按照Post的语义，该操作是会修改服务器上的数据的。

区别二：服务器请求的区别

1、Get请求是可以被缓存的，举个例子，你访问e68a84e8a2ad7a6431333366306432baidu.com，就是向baidu的服务器发了个Get请求，这个请求的返回，也就是baidu的主页页面内容，会被缓存在你浏览器中，短时间再次访问，其实是拿到的浏览器中的缓存内容。另外Get请求只能接收ASCII码的回复

2、Post请求是不可以被缓存的。对于Post方式提交表单，刷新页面浏览器会弹出提示框  “是否重新提交表单”，Post可以接收二进制等各种数据形式，所以如果要上传文件一般用Post请求。

区别三:参数放请求头和请求体的差别

1、Get请求通常没有请求体（当然这也是可以由程序猿心情改变的），在TCP传输中只需传输一次（而不是一个包），所以Get请求效率相对高。

2、Post请求将数据放在请求体中，而实际传输中，会先传输完请求头，再传输请求体，是分为两次传输的（而不是两个包）。Post请求头会比Get更小（一般不带参数），请求头更容易在一个TCP包中完成传输，更何况请求头中有Content-Length的标识，可以更好地保证Http包的完整性。
'''

# 4. post请求有几种数据格式
'''
1、application/x-www-form-urlencoded 
2、multipart/form-data
3、application/json
4、text/xml

'''
