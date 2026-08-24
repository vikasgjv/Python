# Function Caching 

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5) #for reference the gap
    return n*5

#it computes
print(fx(20))
print("done for 20")
print(fx(30))
print("done for 30")
print(fx(200))
print("done for 200")

#it won't compute again  
print(fx(20)) #it is already computed soo it fetch the result from the cache no need to recompute it
print("done for 20")
print(fx(200))
print("done for 200")

#it computes
print(fx(300))
print("done for 300")