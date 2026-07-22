#seek(),tell() & other functions
with open('self.txt','r') as f:

    f.seek(10) #it moves the current position to 10bytes forward
    print(f.tell()) #it tells the current position
    data = f.read(6) #it starts reading after seek...reads 6 bytes from their
    print(data)

#truncate()
with open('self.txt','w') as f:
    f.write("truncate")
    f.truncate(4)