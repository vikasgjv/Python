#how import works

import math #it imports the functions in the module
print(math.sqrt(9)) #but need to use math. everytime whn we call function
print(math.pi)


from math import sqrt,pi #in this  type we can only import sepicified functions from the math module 
result = sqrt(9)*pi     #no need to use math before the function
print(result)

# from math import *     it imports all the  functions into the script (importing everyhting)...not  recommended
                       
#as keyword

import math as m
print(m.sqrt(54)) #insted math we can shortform into m by using math keyword

from math import sqrt as s
print(s(54))

print(dir(math)) #it shows wat all the functions and variables are present in the mmodule

#we can import from our own functions  such as :

 
