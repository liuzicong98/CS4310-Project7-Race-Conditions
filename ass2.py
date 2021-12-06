import threading
import time
import random

#input
n = 50
k = 10
t = 3
buffer = [0 for i in range(n)]
full = 0
empty = n

def P(item):
    global full
    global empty
    if item == "full":
        if full > 0:
            full -= 1
    else:
        if empty > 0:
            empty -= 1

def V(item):
    global full
    global empty
    if item == "full":
        full += 1
    else:
        empty += 1

def Producer():
    global n
    global k
    global t
    global buffer
    global full
    global empty
    next_in = 0
    while 1:
        k1 = random.randint(0, k)
        for i in range(0, k1):
            while empty <= 0:
                pass
            P("empty")
            buffer[(next_in + i % n) % n] += 1
            V("full")
        next_in = (next_in + k1 % n) % n
        t1 = random.randint(0, t)
        print("Producer:",buffer)
        time.sleep(t1)

def Consumer():
    global n
    global k
    global t
    global buffer
    global full
    global empty
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
            while full <= 0:
                pass
            P("full")
            buffer[(next_out + i % n) % n] = 0
            V("empty")
        next_out = (next_out + k2 % n) % n
        print("Consumer:",buffer)

if __name__ == "__main__":
    producer = threading.Thread(target=Producer, daemon=True)
    consumer = threading.Thread(target=Consumer)
    producer.start()
    consumer.start()
