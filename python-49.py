# File IO in Python 

#reading a file
# f = open('Notes.txt','r') #filename , read
# text = f.read()
# print(text)
# f.close()

#writing a file
#whenever you use w-mode to write the data..it firstly clear the previous data inside file and a write a new one.
f2 = open('self.txt','w')
f2.write("created the file through write mode")
f2.close() #important to close the file

#appending a file

f2 = open('self.txt','w') #each time you run the code it appends the text to the file
f2.write("created the file through write mode\n") 
f2.close()

#if you don't wanna close thn you need to use 'with' statement

with open('self.txt','a') as f:
    f.write("by using 'with' statement ")
