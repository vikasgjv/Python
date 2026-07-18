#loops

#for loop

#iterating over a string
name = 'vikas'
for i in name:
    print(i)

#iterating over a list
colors = ["red","yellow","black","orange"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#range function

for k in range(5): # prints from 0 to 4
    print(k)

for k in range(1,11): #prints from 1 to 10
    print(k)

for i in range(0,100,10): #prints in 10 parts in the range of 0 to 100
    print(i)