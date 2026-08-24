#Time Module

import time
print(time.time()) #time in floating point

time.sleep(5)
print("It prints after 5 secs")

t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H:%M:%S",t)
print(formatted_time)