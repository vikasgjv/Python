import time 

current_time = time.strftime('%H,%M,%S')
print(current_time)

hour = int(time.strftime("%H"))
print(hour)

if (hour >0 and hour<12):
    print("Good Moring")
elif (hour>=12 and hour<16):
    print("Good afternoon")
elif(hour>=16 and hour<19):
    print("Good Evng")
else:
    print("Good night")