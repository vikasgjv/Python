# Strings Slicing and Operations on Strings

#length of a string

fruit = "Mango"
print(len(fruit)) #gives total number of characters in the string

#Slicing in String

print(fruit[1:3]) #1 is included and 3 is not included
print(fruit[:4]) #it automatically statrs from the 0th index
print(fruit[1:]) #prints still last
print(fruit[0:-2]) # its actually works as [0:len(fruit)-2] python automatically consider len() and then subtract it