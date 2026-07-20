# dictionaries

dict = {
    # key   :   value
    'netflix' : 'ott platform',
    'flipkart' : 'shopping platform',
    'phonepay' : 'payment platform'
}

print(dict['phonepay'])   #acces the value  of the key
# print(dict['payment platform'])  by giving value you cannot acces the key

print(dict)

print(dict.get('amazon')) #if it not present. shows none

print(dict.keys()) #prints all the key
print(dict.values()) #prints all the values
print(dict.items()) #prints keys with vlaues

for key,value in dict.items():
    print(f"the corresponding value of {key} is {value} ")