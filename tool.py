from queue import Queue
from time import time, sleep
from threading import Thread

def fast(q):
    start_time = time()
    while True:
        x = q.get()
        sleep(0.1)
        print("fast")
        print(x)
        if x >= 19:
            print(time() - start_time)

def slow(q):
    while True:
        x = q.get()
        sleep(1)
        print(x)
        print("shit happen")
        q.put(x)
        sleep(0.2)

q = Queue()
for i in range(20):
    q.put(i)

t1 = Thread(target=fast, args=(q,))
t2 = Thread(target=slow, args=(q,))
#t3 = Thread(target=fast, args=(q,))


t1.start()
t2.start()
#t3.start()