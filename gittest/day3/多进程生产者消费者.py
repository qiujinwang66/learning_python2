from multiprocessing import Process, Queue, Lock
import queue
import time

numconsumers = 20
numproducers = 20
nummessages = 4


def producer(idnum, dataQueue):  # 一个生产者生产四条消息  并且加到dataQueue里面
    for msgnum in range(nummessages):
        dataQueue.put("producer id=%d, count=%d" % (idnum, msgnum))  # 加到dataQueue里面

def consumer(idnum, dataQueue, lock):
    while True:
        try:
            data = dataQueue.get(block=False) #  消费者去 dataQueue 取值，如果是false 跳出循环  这里如果写true的话就不能自动跳出，就会一直等待生产者生产的东西，卡死了
        except queue.Empty:   #  如果异常报错
            break
        with lock:                            # 消费者去 dataQueue 取值，如果有值 就添加到队列中
            print("consumer", idnum, "got => ", data)
        time.sleep(0.1)


if __name__ == "__main__":
    lock = Lock()
    dataQueue = Queue()
    consumers = []
    producers = []
    for i in range(numproducers):
        p = Process(target=producer, args=(i,dataQueue))
        producers.append(p)
        p.daemon = True
        p.start()
    for i in range(numconsumers):
        p = Process(target=consumer, args=(i,dataQueue,lock))
        consumers.append(p)
        p.daemon = True
        p.start()

    for p in consumers:
        p.join()
    for p in producers:
        p.join()
