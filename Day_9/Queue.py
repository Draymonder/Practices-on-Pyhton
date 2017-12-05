from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print("写数据进程开启!")
    for value in ['A', 'B', 'C', 'D']:
        print("put %s into queue" % value)
        q.put(value)
    time.sleep(random.random())


def read(q):
    print("读数据进程开启!")
    while not q.empty():
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))

    pw.start()
    pr.start()

    pw.join()

