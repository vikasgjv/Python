#string

name = "Vikas"
python = 'hello'

#for multiline string 
s = """ numerating objects: 5, done.
Counting objects: 100% (5/5), done.   
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 300 bytes | 300.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
"""

#indexing 
print(name[0])
print(python[3])

#Looping in String
for character in name:
    print(character)

for i in s:
    print(i)


