# for Loop with else

for i in range(6):
    print(i)
else:
    print("loop ended")


for j in range(8):
    print(j)
    if j ==3:
        break #it breaks / stops the loop here itself ..dont let to reach the else clause.
else:
    print("loop ended")


#while loop with else

i =0
while(i<7):
    print(i)
    i+=1
else:
    print("i reached till 6")


j =0
while(j<7):
    print(j)
    j+=1
    if j ==5:
        break
else:
    print("j reached till 6")