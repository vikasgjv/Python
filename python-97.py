# Multithreading

import time
import threading

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# Normal Code
func(4)
func(2)
func(1)

# Same code using Threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()
 