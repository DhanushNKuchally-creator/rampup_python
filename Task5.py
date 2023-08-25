import threading
import time
import random
import queue

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

def producer(iterations):
    items = ['a', 'b', 'c']
    for _ in range(iterations):
        item = random.choice(items)
        q.put(item)
        print(threading.current_thread().name, 'Putting', str(item), ':', str(q.qsize()), 'items in queue')
        time.sleep(1)

def consumer(iterations):
    for _ in range(iterations):
        if not q.empty():
            item = q.get()
            print(threading.current_thread().name, 'Getting', str(item), ':', str(q.qsize()), 'items in queue')
        time.sleep(1)

if __name__ == '__main__':
    iterations = int(input("Enter the number of iterations: "))

    p = threading.Thread(target=producer, args=(iterations,), name='producer')
    c = threading.Thread(target=consumer, args=(iterations,), name='consumer')

    p.start()
    time.sleep(0.5)
    c.start()
    p.join()
    c.join()



    
