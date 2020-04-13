import threading,queue
import time

numconsumers = 20
numproducers = 20
nummessages = 4


lock = threading.Lock()
dataQueue = queue.Queue()

def producer(idnum):  # 一个生产者生产四条消息  并且加到dataQueue里面
    for msgnum in range(nummessages):
        dataQueue.put("producer id=%d, count=%d" % (idnum, msgnum))  # 加到dataQueue里面

def consumer(idnum):
    while True:
        try:
            data = dataQueue.get(block=False) #  消费者去 dataQueue 取值，如果是false 跳出循环  这里如果写true的话就不能自动跳出，就会一直等待生产者生产的东西，卡死了
        except queue.Empty:   #  如果异常报错
            break
        with lock:                            # 消费者去 dataQueue 取值，如果有值 就添加到队列中
            print("consumer", idnum, "got => ", data)
        time.sleep(0.1)
        dataQueue.task_done()

if __name__ == "__main__":
    #consumerThreads = []
    #producerThreads = []
    for i in range(numproducers):
        t = threading.Thread(target=producer, args=(i,))
        #producerThreads.append(t)
        t.start()

    for i in range(numconsumers):
        t = threading.Thread(target=consumer, args=(i,))
        #consumerThreads.append(t)
        t.start()

    dataQueue.join()
