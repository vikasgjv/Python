# tuples

tup = (1,2,3,4,4,5,'python')
print(type(tup) , tup)

print(tup[0])
print(len(tup))
print(tup[-2])

if 3 in tup:
    print("yes")

#slicing
print(tup[1:3]) 
print(tup)

# Operations on Tuples

#to-do operations on tuple you convert to list and thn back to tuple
tup = ('india','russia','japan','italy','iran','usa')
temp = list(tup)
temp.append('srilanka')
temp.remove('iran')
tup = tuple(temp)
print(tup)

#concatination 

tup2=('delhi','london','germeny')
tup3 = tup +tup2
print(tup3)

print(tup.count('india'))
print(tup.index('india'))

print(len(tup3))

'''
if you want to add,remove,change the tuple thn you must convert the tuple to a list and perfrom the operations in the list 
					   later the list back to the tuple. --> temp = list(tup)
                       '''