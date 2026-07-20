# Set Methods

s1 = {1,9,4,3}
s2 = {0,2,1,3}

print(s1.union(s2)) #union function combines the values
s1.update(s2) #it copys the elemnts from from s2 to s1
print(s1) 


cities = {'delhi','mumbai','banglore','chennai'}
cities2 =  {'delhi','mumbai','hyderbad','ladak'}
print(cities.intersection(cities2)) #common elements
cities.intersection_update(cities2) #keeps only common elements in cities
# print(cities)


s3 = {101,320.112,101,100,320}
s4 = {102,101,319,100}
print(s3.symmetric_difference(s4)) #prints items that are not similar bascially  prints uniques items
s3.symmetric_difference_update(s4) #it removes the elelments common in s4
print(s3)


 
cities3 = {'delhi','mumbai','banglore','chennai'}
cities4 =  {'delhi','mumbai','hyderbad','ladak'}
print(cities3.difference(cities4)) #prints items that are only present in original set not in both the sets
cities3.difference_update(cities4) #it updates the cities3 set
print(cities3) 

cities5 = {'delhi','mumbai','banglore','chennai'}
cities6 =  {'delhi','mumbai' }
print(cities5.isdisjoint(cities6)) #checks all the items are unique in cities5 compared to cities6
print(cities5.issuperset(cities6)) #checks if all the items in citites6 are present in cities5
print(cities6.issubset(cities5)) #subset

cities5.add('goa') #adds items
print(cities5)
cities5.update(cities4) #adds elemnets of cities4 to citites5
print(cities5)

cities5.remove('goa') #removes item ..if the item not present in the set it rises an error
print(cities5)
cities5.discard('goa')  #removes item ..if the item not present in the set it doesn't rises an error
print(cities5)

print(cities5.pop()) #removes a random item in a set bcz sets are unordered

del cities5 #deletes the entire set
 
cities6.clear() #clears the entries set..basically makes it an empty set
print(cities6)

if 'delhi' in cities:
    print('present')
else:
    print('not present')