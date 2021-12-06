import threading
import time
import random

#input
n = 50
k = 10
t = 3
buffer = [0 for i in range(n)]

def Producer():
    global n
    global k
    global t
    global buffer
    next_in = 0
    while 1:
        k1 = random.randint(0, k)
        for i in range(0, k1):
            buffer[(next_in + i % n) % n] += 1
        next_in = (next_in + k1 % n) % n
        t1 = random.randint(0, t)
        print("Producer:",buffer)
        time.sleep(t1)

def Consumer():
    global n
    global k
    global t
    global buffer
    next_out = 0
    while 1:
        t2 = random.randint(0, t)
        time.sleep(t2)
        k2 = random.randint(0, k)
        for i in range(0, k2):
            data = buffer[(next_out + i % n) % n]
            if data > 1:
                print("Race condition:",buffer)
                return
            buffer[(next_out + i % n) % n] = 0
        next_out = (next_out + k2 % n) % n
        print("Consumer:",buffer)

if __name__ == "__main__":
    producer = threading.Thread(target=Producer, daemon=True)
    consumer = threading.Thread(target=Consumer)
    producer.start()
    consumer.start()
