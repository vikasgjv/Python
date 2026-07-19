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