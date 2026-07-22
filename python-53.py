# Map, Filter and Reduce
l = [1,2,3,4,5]
#map
def cube(x):
    return x * x * x

 

l2 = list(map(cube,l)) #maps each l value to the function
print(l2)
#using lambda
ans = list(map(lambda x : x*x*x ,l))
print(ans) 

#filter
def fil(a):
    return a >3

l3 = list(filter(fil,l))
print(l3)

#reduce
from functools import reduce
num = [1,2,3,4,5,6]

res =  reduce(lambda x,y : x+y,num) #it adds first 2 elemts and then the sum with the third element
print(res)