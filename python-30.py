#Recursive function

'''
factorial 
        factorial 0f 5 : 5*4*3*2*1
        factorial 0f 4 : 4*3*2*1
        factorial 0f 3 : 3*2*1
        factorial 0f 2 : 2*1
        factorial 0f 1 : 1
        factorial 0f 0 : 1 (default)

        here we can obsserve that factorial means n * n-1 
'''
 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) #factorial (n-1) prints the remaing numbers 

print(factorial(5))

'''
5*factorial (4)
5*4*factorial(3)... 
'''

#fibnooci series

# 0,1,1,2,3,5,8,13,21...... sum precedings.

def fibonacci(n):
    if n ==0 or n==1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


