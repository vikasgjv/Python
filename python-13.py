# String Methods

#strings are immutable 

a = "Virat kholi !!!"
print(a.upper())
print(a.lower())
print(a.rstrip('!')) #remove ! only in the ending
print(a.replace("kholi","Anshuska")) #it repalce

b = "hii , how Are yOu guyss"
print(b.split()) #it ffroms a list 
print(b.capitalize()) #it forms sentence in a perfert mannner (converts frist leeter to uppercase and other letters to lowercase)

print(a.center(50)) #it prints in the center

print(b.count("h")) #it prints number of occurneces

#endswith()

print(b.endswith("ss")) #it returns in boolean
print(b.endswith("ii" ,1,3)) #endswith(suffix, start, end)

print(a.find("kholi")) #it returns the index of the first occurence
print(a.find("vikas")) #returns -1 if not found

str = "macbook air m"
print(str.isalnum())
print(str.isalpha())
print(str.islower())
print(str.isupper())

#swapcase
print(b.swapcase()) #its swaps upper to lowers ..vicevers

print(b.title()) #in title formss