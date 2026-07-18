# break and continue

#break - terminate the loop
for i in range(1,15):
    print("10 X ",i,"=",10*i)
    if(i==10):
        break

print("Loop ko chodkar nikal gaya")

#continue - skips the iteration

for i in range(1,13):
    if i ==11:
         print("skipped the loop -11th")
         continue
    print("10 X ",i,"=",10*i)

#do while loop in py(not mandatory just know about it )

i =0
while True:
    print(i)
    i=i+1
    if(i>10):
        breaks