#Lambda functions

# def pow(x,y):
#     return x**y

# print(pow(2,3))

#insted creating a  function we can use  
       #lambda argument : expression
power = lambda x , y : x**y
print(power(2,3))

x = int(input("enter a number for cube : "))
cube = lambda x : x*x*x
print(cube(x))

#we can also lambda function into another function

def sum(fun,value):
    return 6 +fun(value)

print(sum(lambda x:x*x , 2)) #lambda expression and the value both passed to the function sum