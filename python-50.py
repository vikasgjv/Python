# read(), readlines() and other methods

f = open('self.txt','r')
l = f.readline()
print(l) #prints only single line from the file

#by using loop we can read multiple lines

while(True):
    lines = f.readline()
    if not lines:
        break
    print(lines)


#writelines()
f = open('self.txt','w')
w = ['line 1 \n','line 2\n','line 3']
f.writelines(w)
f.close()


