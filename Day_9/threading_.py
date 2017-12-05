import time, threading,random

# 线程1执行的代码:
def loop1():
    i = 0
    while i <= 10:
        print("the number is : %s " % i)
        time.sleep(random.random())
        i += 1

# 线程2执行的代码:
def loop2():
    i = 0
    while i <= 100:
        print("the number is : %s " % i)
        time.sleep(random.random())
        i += 10

t1 = threading.Thread(target=loop1)
t2 = threading.Thread(target=loop2)
t1.start()
t2.start()
t1.join()
t2.join()
