#Function Arguments

#defeault arguments 

def name(fname = "s",mname = 's',lname='rajmouli'): 
    print(fname +mname +lname)

name('r')  #if doesnt provide any value it consdiers defult value in the function

#keyword arguments 

def num(a=3,b=2):
    print(a-b)

num(a=10,b=5) #sepicifing the values with key=value


#required arguments

def sum(a,b=1):
    print(a+b)
sum(a=1) #here a is the requried argument

#variable length arguments

def avg(*numbers): #it creats a tuple of values 
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum+i
    print(sum/len(numbers))

avg(1,2,3,4,5,6,7,8,9,10)


def name(**name): #it creats a dict
    print(type(name))
    print("hello",name['fname'] + name['mname'] + name['lname'])

name(mname ='rocky',fname = 'yash',lname = 'bhai')

#return statement

def expo(a,b):
    return a**b 
    return a+b #it ignores the second return it only consoders the first return

a,b = 2,5
c=expo(a,b)
print(c)
