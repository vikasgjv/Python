# Regular Expressions

import re

pattern = 'was'
text = '''Brochfael ap Meurig (ruled c. 872 – c. 910) was the king of Gwent in south-east Wales. He ruled jointly with his brother, Ffernfael ap Meurig. Gwent and Glywysing, the neighbouring territory to the west, were ruled as a single kingdom in some periods; at other times they were separate and the king of Glywysing had the higher status. Brochfael's father, Meurig ab Arthfael, ruled both territories with the title of King of Glywysing, but Brochfael and Ffernfael were only kings of Gwent, and had a lower status than their cousin Hywel ap Rhys, the king of Glywysing. The Anglo-Saxon kingdom of Mercia claimed dominion over most of Wales, but in the late 880s Brochfael, Ffernfael and Hywel submitted voluntarily to Alfred the Great, the king of Wessex, in order to gain protection from the oppression of Æthelred, Lord of the Mercians. A number of Brochfael's charters survive, mainly grants to Bishop Cyfeilliog and settlements of Brochfael's disputes with the bishop. Brochfael was the last of his line and was succeeded by Hywel's son'''

match = re.search(pattern , text)
print(match)


# 1. Exact word
pattern = r'was'
print(re.findall(pattern, text))

# 2. [] - Character class
pattern = r'[Ww]as'
print(re.findall(pattern, text))

# 3. | - OR operator
pattern = r'was|were'
print(re.findall(pattern, text))

# 4. . - Any character
pattern = r'w.s'
print(re.findall(pattern, text))

# 5. ? - Zero or one occurrence
pattern = r'was?'
print(re.findall(pattern, text))

# 6. * - Zero or more occurrences
pattern = r'wa*s'
print(re.findall(pattern, text))

# 7. + - One or more occurrences
pattern = r'wa+s'
print(re.findall(pattern, text))

# 8. {} - Specific number of occurrences
pattern = r'w{1}'
print(re.findall(pattern, text))

# 9. ^ - Starts with
pattern = r'^Brochfael'
print(re.findall(pattern, text))

# 10. $ - Ends with
pattern = r'territories\.$'
print(re.findall(pattern, text))

'''
[] — Represent a character class
^ — Matches the beginning
$ — Matches the end
. — Matches any character except newline
? — Matches zero or one occurrence
| — Means OR (matches any of the characters separated by it)
* — Any number of occurrences (including 0 occurrences)
+ — One or more occurrences
{} — Indicate the number of occurrences of a preceding RE
'''