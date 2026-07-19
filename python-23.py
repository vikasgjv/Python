# List Methods

list = [20,43,22,10,35,0,7,9,2005,18]

list.sort() #ascending order
print(list)

list.append(32) #adds to last
print(list)

list.sort(reverse=True) #descending order
print(list)

list.reverse() #reverse it 
print(list)

print(list.index(2005)) #gives index of 2005

list.insert(0,"v7") #insert the value v7 at index 0
print(list)

list2 = ['virat','abd','salt','bhuvi'] 
list.extend(list2) #extends space in list and the values to it
print(list) 

list3 = ['RCB']
final = list + list3 #concatenation
print(final)

final.remove(32)
print(final)

print(len(final))


list2 = ['virat','abd','salt','bhuvi'] 
list.extend(list2) #extends space in list and the values to it
print(list) 

